import argparse
import os
import pkgutil
import inspect
from . import commands
from  importlib import import_module

#Package where commands are located
PACKAGE = "gateway.commands"

DESCRIPTION = "Collects and Recieves and Analyzes Data"

parser = argparse.ArgumentParser(description=DESCRIPTION)
listOfCommands = {}


def loadCommandModules():
    modules = pkgutil.iter_modules([os.path.dirname(commands.__file__)])
    for module in modules:
        listOfCommands[module[1]] = import_module('.' + module[1], PACKAGE)

    parser.add_argument('service', choices=listOfCommands.keys())
    try:
        executeCommand()
    except ClassNonExistent as e:
        print(str(e) + " " + e.errors)

#loadCC - load Command content
def loadCC():
    pass

def executeCommand():
    args = parser.parse_args()

    if args.service not in listOfCommands:
        parser.print_help()
        parser.exit()

    commandModule = listOfCommands[args.service]
    members = inspect.getmembers(commandModule, inspect.isclass)
    commandclass = list(filter(lambda name: name[0].upper() == args.service.upper() + "COMMAND" , members))
    if not commandclass:
        raise ClassNonExistent("Could not find the command class", args.service.capitalize() + "Command")

    commandClass = getattr(commandModule, commandclass[0][0])
    print(commandclass)
    commandClass().run()
class ClassNonExistent(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors



loadCommandModules()
