from evtcantools.dbcmaker import DataBaseMaker
from gateway.utils.resourcelocator import ResourceLocator
from evtcantools.dbcparser import INTEL, MOTOROLA
from gateway.can.configuration import Configuration
import collections

#Author: Daniel Harrington
#Date: 4/8/2017
#Module builds EVT devices and caches their characteristics for distrubution between
#controllers
#
#
# fetchDevice - fetch the device. If device is not in cache construct it and
# its attributes
#
####Device attributes###
#
#MessageBox- defines the messages and theirs signals. A signal operation has
#been defined for each message to perform data extraction
#

class DeviceCache(object):
    devices = {}
    dbcDescriptor = None
    masterMessageBox = {}

    def hasDevice(self,device):
        return device in self.devices

    def __getattr__(self,key):
        return self.devices[key]

    # TODO: deinit the cache after all bindings and configurations are finalized

class SignalBox(object):
    """
    The signalBox is the ultimate object passed around in evt received messages.
    The DeviceConstruct will build a messageBox for a specific device's messages. Each message
    contains a variable amount of signals. Each signal box represents the signals
    that can be pulled out.

    For example if a message box is created for BMS0, then BMS0_module_voltages5
    is a message that would contain signals for battery voltages 17-20.
    To reference these voltages, one may use the direct attribute name eg.
        BMS0_module_voltages5instance.voltage17


    """
    def __init__(self,data):
        self.data = data

    def __str__(self):
        return " Message: " + self.__class__.__name__ +  " data:" + str(self.data)

class MessageBox(object):
    """
    Holds the necessary conversions for a message's signals.

    Each message has a variable amount of signals. Determine where in the data should the necessary
    operations be applied to covert the data to a sensible number.

    Messages can be obtained by either the message name or the canID
    """
    def __init__(self,descriptor):
        self.messages = {}
        self._buildSignals(descriptor)
    def __getattr__(self,value):
        pass
    def signalOp(self,startBit,length):
        """
        a data extraction function for a specific signal as Motorala formatted
        """
        return lambda instance :  (((instance.data >> (63 - startBit)) & ((1 << length) - 1 )))
    def signalOpIntel(self,startBit,length):
        """
         a data extraction function for a specific signal as intel formatted
        """

        return lambda instance :  (((instance.data >> startBit) & ((1 << length) -1 )))

    def _buildSignals(self, messageDescriptor):
        """
        For each message build the signalbox dynamically.
        """
        for messageDscription in messageDescriptor:
            sigfs = {}
            for signal in messageDscription._signals:
#                Motorala format is weird. Lets covert the starbit to an appropriate value
                if signal._format == MOTOROLA:
                    mod = ((signal._startbit + 1 ) % 8)
                    if mod is 0:
                        mod = 8
                    msb = signal._startbit - (signal._startbit % 8) + 8 - mod
                    lsb =  msb + signal._length - 1
                    sigfs[signal._name] = self.signalOp(lsb, signal._length)
                else:
                    sigfs[signal._name] = self.signalOpIntel(signal._startbit, signal._length)

            signalClass = type(messageDscription._name,(SignalBox,), sigfs)

            DeviceCache.masterMessageBox[messageDscription._canID] = signalClass
            DeviceCache.masterMessageBox[messageDscription._name] = signalClass

            self.messages[messageDscription._canID] = signalClass
            self.messages[messageDscription._name] = signalClass

class DeviceConstruct(object):
    """
    Helps parse the signals of devices on the evt network.
    """
    __device_cache = DeviceCache()
    def __init__(self):
        self.configFileLocator = ResourceLocator.get_locator('config/edsfiles')
        if  Configuration.config.eds_file_name() is not None:
            path = self.configFileLocator.fetch_file_path(Configuration.config.eds_file_name())
            self.__device_cache.dbcDescriptor = DataBaseMaker().db_from_path(path)
        else:
            self.__device_cache.dbcDescriptor = DataBaseMaker().db_from_repo()

        self.__device_cache.dbcDescriptor.Load()

    def fetchDevice(self,deviceName):
        if self.__device_cache.hasDevice(deviceName):
            return getattr(self.__device_cache, deviceName)
        else:
            return self.constructDevice(deviceName)

    def fetchDatabase(self):

        return  self.__device_cache.dbcDescriptor
    def constructDevice(self,deviceName):
        """
        returns a message box representing the devices messages and each messages
        signals.
        """
        deviceDescriptor = self.__device_cache.dbcDescriptor._txNodes[deviceName]
        if deviceName not in self.__device_cache.devices:
            self.__device_cache.devices[deviceName] = MessageBox(deviceDescriptor)

        return self.__device_cache.devices[deviceName]


    def masterMessageBox(self):
        for device_name in self.__device_cache.dbcDescriptor._txNodes:
            self.__device_cache.devices[device_name] = MessageBox(self.__device_cache.dbcDescriptor._txNodes[device_name])
        return self.__device_cache.masterMessageBox

    def clearCache(self):
        self.__device_cache = None
