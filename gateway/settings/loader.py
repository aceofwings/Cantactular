from gateway.settings.configurations import Configuration
from gateway.can.interface import Interface
from gateway.can.controller import Controller
#Load the interfaces defined in the Settings  class
# Throws errors on whether it as sucessfully initialize all interfaces


class Resource():
    pass

_resources = Resource()
_resources.interfaces = None
_resources.superControllers = None

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

    _resources.interfaces = interfaces

## these are the controllers our users inherit from to gain access to writing
## to an interface
def associate(controller):
    if _resources.interfaces is None:
        return # should raise or log error
    if controller.interface is not None:
        return
    for interface in _resources.interfaces:
        if issubclass(controller.__class__,interface.ct):
            controller.associateInterface(interface)
            return
# build the controller, if there is no interface associate one, then continue
#to build the controller using helper method. prepareforStart will ready interfaces
# to be luanched
def buildController(controller):
        if controller.interface is None:
            associate(controller)
        shouldstartInterface = controller.buildController()
        if shouldstartInterface or Configuration.forceStartInterfaces:
            controller.interface.start()


def startInterfaces():
    if not _resources.interfaces:
         loadInterfaces()
    for interface in _resources.interfaces:
        interface.start()





class LoadableInterfaces(Exception):
    def __init__(self, message, errors):
        super(LoadableInterfaces, self).__init__(message)
        self.errors = errors
class ImproperControllerDefinition(Exception):
    def __init__(self, message, errors):
        super(ImproperControllerDefinition, self).__init__(message)
        self.errors = errors
