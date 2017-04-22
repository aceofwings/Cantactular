from gateway.settings.configurations import Configuration
from gateway.evtcan.device_construct import DeviceConstruct
from gateway.can.interface import Interface
from gateway.can.controller import Controller
from gateway.core.systemlogger import logger
from gateway.utils.projectpaths import common
from gateway.core.systemlogger import RunRotatingtHandler
import logging
import logging.handlers
#Author Daniel Harrington
#Date - 4/8/2017
#Loader module is responsible for loading resources to be used the rest of the app
#build process
#
#
#The loader and its resources can be built customily with the use of
#Configurations.py
#
#
# Loads the interfaces and assigns the base controllers specified in configurations.py
#
# Builds the controller, and additional needed attributes upon start of interfaces
#
# Starts the interface based on the controller build function or the forceStartInterfacee
# in Configurations.py
#
class Resource():
    pass
#cached resources shared through the program build process
_resources = Resource()
_resources.interfaces = None
_resources.busInterfaceNames = None
_resources.superControllers = None
_resources.deviceConstruct = None

def loadLogger():
    logger = logging.getLogger('gateway')
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(' %(levelname)s - %(message)s')
#    fileHandler = logging.FileHandler(common.log + "/track.log")
    fileHandler = RunRotatingtHandler(common.log + "/track.log", freshRun = Configuration.freshLogFileOnRun)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)


def devicesInfo():
    logger.info("Configuring Device Mapping %s", Configuration.imediateLoadDevice)

def loadDevices():
    devicesInfo()
    if Configuration.imediateLoadDevice is None:
        return
    if _resources.deviceConstruct is None:
        _resources.deviceConstruct = DeviceConstruct(Configuration.maindbcFile)
    for deviceName in Configuration.imediateLoadDevice:
        _resources.deviceConstruct.constructDevice(deviceName)

def mapInterfaceNames():
    _resources.busInterfaceNames = list(Configuration.interfaceNames.keys())

def loadInterfaces():
    interfaces = []
    mapInterfaceNames()
    faces = Configuration.interfaceNames
    #associate an interface name with a controllerType. This ultimately
    #determines the protocol each interface will be using
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

# associate a controller with the correct interface
def associate(controller):
    if _resources.interfaces is None:
        loadInterfaces()
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
