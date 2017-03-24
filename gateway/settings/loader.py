from gateway.settings.configurations import Configuration
from gateway.can.interface import Interface
from gateway.can.controller import Controller
#Load the interfaces defined in the Settings  class
# Throws errors on whether it as sucessfully initialize all interfaces
def loadInterfaces():
    interfaces = []
    faces = Configuration.interfaceNames

    for faceName, controllerType in faces.items():
        interface = Interface(faceName)

        if issubclass(controllerType, Controller):
            interface.ct = controllerType
        else:
            if Configuration.failureSilence:
                interface.ct = Controller
            else:
                raise ImproperControllerDefinition("Unfamliar Controller Type", errors = None)


        interfaces.append(interface)

    if not interfaces:
        raise LoadableInterfaces("No interfaces could be found", None)

    return interfaces


class Associator(object):
## these are the controllers our users inherit from to gain access to writing
## to an interface
    def __init__(self, interfaces):
        self.interfaces = interfaces
        self.superControllers = [interface.ct for interface in interfaces]

    def asssociate(self,controller):
        if interfaces is None:
            return # should raise or log error
        if controller.interface is not None:
            return
        for interface in interfaces:
            if issubclass(controller,interface.ct):
                controller.associateInterface(interface)
                return





class LoadableInterfaces(Exception):
    def __init__(self, message, errors):
        super(LoadableInterfaces, self).__init__(message)
        self.errors = errors
class ImproperControllerDefinition(Exception):
    def __init__(self, message, errors):
        super(ImproperControllerDefinition, self).__init__(message)
        self.errors = errors
