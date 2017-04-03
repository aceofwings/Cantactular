from gateway.evtcan.dbcParser import CANDatabase


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

        return __device.dbcDescriptor._txNodes[deviceName]
