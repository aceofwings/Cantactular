from gateway.evtcan.dbcParser import CANDatabase
from gateway.can.device import EvtCanDevice

class DeviceCache(object):
    devices = {}
    dbcDescriptor = None
    def hasDevice(self,device):
        return device in devices

    def __getattr__(self,key):
        return devices[key]

    # TODO: deinit the cache after all bindings and configurations are finalized
""" cache file operations and device configurations """
__device_cache = DeviceCache()


class MessageBox(object):
    def __init__(self):
        self.messages = None


    def __getattr__(self,value):
        pass
    """IMPORT NOTE - Make sure is unpacked as little endian format"""
    def _buildSignals(self, messageDescriptor):
        sigfs = {}
        for messageDscription in messageDescriptor:
                for signal in messageDscription:
                    f = lambda data :  (((data >> signal._startbit) & math.pow(2,signal._length)))
                    sigfs[signal._name] = f
        return sigfs

class DeviceConstruct():

    def __init__(self,dbcfileName):
        self.dbc = dbcfileName

    @classmethod
    def fetchDevice(self,deviceName):
        if __device_cache.hasDevice(deviceName):
            return getattr(__device_cache, deviceName)
        else:
            self.constructDevice(deviceName)
        return  getattr(__device_cache, deviceName)

    def constructDevice(self,deviceName):
        if __device_cache.dbcDescriptor is None:
            __device.dbcDescriptor = CANDatabase(self.dbc)
            __device.dbcDescriptor.load()

        deviceDescriptior = __device.dbcDescriptor._txNodes[deviceName]

        __device_cache[deviceName] = deviceDescriptior

        deviceDescriptors = Descript
        evtDevice = EvtCanDevice()
