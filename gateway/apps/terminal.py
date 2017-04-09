
from gateway.utils.projectpaths import ProjectPath
from gateway.opencan.opencancontroller import CanOpenController
from gateway.evtcan.controller import EvtCanController
from gateway.can.message import CanMessage
from gateway.can.listener import Listener
from gateway.can.device import CanOpenDevice
from gateway.settings.loader import buildController
from gateway.evtcan.device_construct import DeviceConstruct



#may want to inherit from our own custom code
class Terminal(object):

    def __init__(self):
        super()
        term = TermEvtCanController()
        buildController(term)
        while True:
            pass

    def start(self):
        pass

class TermEvtCanController(EvtCanController):

    def __init__(self):
        super().__init__()
        self.bms = None
    def buildController(self):
        super().buildController()
        construct = DeviceConstruct("test_EVT_CAN.dbc")
        device = construct.fetchDevice("BMS")
        self.addDevice(device)

        return True

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
