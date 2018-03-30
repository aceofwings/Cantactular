import inspect
import pkgutil
import sys

from gateway.can.controllers.base import BaseController, OPENCAN, EVTCAN
from gateway.evtcan.matcher import EvtCanMatcher
from gateway.can.control.matcher import OpenCanMatcher

class ControllerBox(object):
    controller_definitons = []
    controllers = []
    handlers = {}

def fetch_controllers(controller_space):
    """
    go through each file and find controller_definitons, if a controller definiton
    exists add it to the controller box.
    """
    cb = ControllerBox()
    for importer, module_name, ispkg in pkgutil.iter_modules(controller_space.__path__):
        module = importer.find_module(module_name).load_module(module_name)
        for module_member in inspect.getmembers(module, inspect.isclass):
            if issubclass(module_member[1], BaseController):
                cb.controller_definitons.append(module_member[1])
    return cb

def build_controllers(controller_definitions):
    """
    loop through the list of controller definitions creating them.
    """
    c_list = []
    for controller_definition in controller_definitions:
        c_list.append(controller_definition())
    return c_list

def load_handlers(controllers):
    """
    Load the controllers handlers and assign them to the instance
    """
    handlers = {}
    for controller in controllers:
        for handler in controller.build_controller():
            if handler.type in handlers:
                handlers[handler.type].append(handler)
            else:
                handlers.setdefault(handler.type,[])
                handlers[handler.type].append(handler)
    return handlers


def create_matchers(handlers):
    """
    Assign each type of handled to there designated matcher
    """
    matchers = [OpenCanMatcher,EvtCanMatcher]
    for matcher in matchers:
        if matcher.match_type in handlers:
            matcher.handlers = handlers[matcher.match_type]


def load_controllers(controller_space):
    controller_box = fetch_controllers(controller_space)
    controller_box.controllers = build_controllers(controller_box.controller_definitons)
    controller_box.handlers = load_handlers(controller_box.controllers)
    create_matchers(controller_box.handlers)
