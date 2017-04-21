
from gateway.opencan.opencancontroller import CanOpenController
from gateway.evtcan.controller import EvtCanController
from gateway.can.device import CanOpenDevice
from gateway.settings.loader import buildController



#may want to inherit from our own custom code
class Terminal(object):

    def __init__(self):
        super()
        term = TermEvtCanController("INTEL_EVT_CAN.dbc")
        buildController(term)
        while True:
            pass

    def start(self):
        pass

class TermEvtCanController(EvtCanController):

    def buildController(self):
        super().buildController()
        self.setupListener()
        bms = self.devices.fetchDevice("BMS0")
        self.addDevice(bms)
        self.addDevice(self.devices.fetchDevice("IMU"))
        self.controllerListener.addHandler('all',self.handleBroadCast)
        return True

    def handleBroadCast(self,nodeID, evtMessage):
        evtMessage.cool()


class TermOpenController(CanOpenController):

    def __init__(self):
        super().__init__()
        self.controllerListener.addHandler(0x00,self.handleBroadCast)

    def buildController(self):
        super().buildController()
        self.motor = CanOpenDevice(0x01,"MotorController")
        self.addDevice(self.motor)
        return True

    def handleBroadCast(self,nodeID,value):
        print("Handle BroadCast")
