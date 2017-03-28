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


## these are the controllers our users inherit from to gain access to writing
## to an interface
def associate(controller):
    if interfaces is None:
        return # should raise or log error
    if controller.interface is not None:
        return
    for interface in interfaces:
        if issubclass(controller.__class__,interface.ct):
            controller.associateInterface(interface)
            ## not so subtle fix will design for apropriate launch
            controller.buildController()
            return




    #from Configuration


interfaces = loadInterfaces()
superControllers = [interface.ct for interface in interfaces]


class LoadableInterfaces(Exception):
    def __init__(self, message, errors):
        super(LoadableInterfaces, self).__init__(message)
        self.errors = errors
class ImproperControllerDefinition(Exception):
    def __init__(self, message, errors):
        super(ImproperControllerDefinition, self).__init__(message)
        self.errors = errors
