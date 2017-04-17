from gateway.evtcan.dbcParser import CANDatabase
from gateway.can.device import EvtCanDevice
import collections

#Author: Daniel Harrington
#Date: 4/8/2017
#Module builds EVT devices and caches their characteristics for distruution between
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

    def hasDevice(self,device):
        return device in self.devices

    def __getattr__(self,key):
        return self.devices[key]

    # TODO: deinit the cache after all bindings and configurations are finalized
""" cache file operations and device configurations """

class MessageBox(object):
    def __init__(self,descriptor):
        self.messages = {}
        self._buildSignals(descriptor)
    def __getattr__(self,value):
        pass
    def signalOp(self,startBit,length):
        return lambda data :  (((data >> (63 - startBit)) & ((1 << length) - 1 )))
    """Build Signal for Motorola format"""

    def _buildSignals(self, messageDescriptor):
        for messageDscription in messageDescriptor:
            sigfs = {}
            for signal in messageDscription._signals:
# Motorala format is weird. Lets covert the starbit to an accepted start value
                mod = ((signal._startbit + 1 ) % 8)
                if mod is 0:
                    mod = 8
                msb = signal._startbit - (signal._startbit % 8) + 8 - mod
                lsb =  msb + signal._length - 1
                sigfs[signal._name] = self.signalOp(lsb, signal._length)

            self.messages[messageDscription._canID] = collections.namedtuple('signal',sigfs.keys())(**sigfs)
            self.messages[messageDscription._name] = collections.namedtuple('signal',sigfs.keys())(**sigfs)
class DeviceConstruct(object):

    __device_cache = DeviceCache()

    def __init__(self,dbcfileName):
        self.dbc = dbcfileName

    def fetchDevice(self,deviceName):
        if self.__device_cache.hasDevice(deviceName):
            return getattr(self.__device_cache, deviceName)
        else:
            return self.constructDevice(deviceName)

    def fetchDatabase(self):
        if self.__device_cache.dbcDescriptor is None:
            self.__device_cache.dbcDescriptor = CANDatabase(self.dbc)
            self.__device_cache.dbcDescriptor.Load()

        return  self.__device_cache.dbcDescriptor
    def constructDevice(self,deviceName):
        if self.__device_cache.dbcDescriptor is None:
            self.__device_cache.dbcDescriptor = CANDatabase(self.dbc)
            self.__device_cache.dbcDescriptor.Load()

        deviceDescriptor = self.__device_cache.dbcDescriptor._txNodes[deviceName]


        evtDevice = EvtCanDevice()
        evtDevice.messageBox = MessageBox(deviceDescriptor)
        self.__device_cache.devices[deviceName] = evtDevice

        return evtDevice
