
from gateway.utils.projectpaths import ProjectPath
from gateway.opencan.opencancontroller import CanOpenController
from gateway.can.message import CanMessage
from gateway.can.listener import Listener
from gateway.can.device import CanOpenDevice
from gateway.settings.loader import associate




#may want to inherit from our own custom code
class Terminal(object):

    def __init__(self):
        super()
        term = TermOpenController()
        associate(term)
        term.setupListener()
        term.interface.start()
        while True:
            pass




    def start(self):
        pass


class TermOpenController(CanOpenController):


    def __init__(self):
        super().__init__()
        self.motor = CanOpenDevice(0x01,"MotorController")
        self.addDevice(self.motor)
        self.controllerListener.addHandler(0x00,self.handleBroadCast)

    def handleBroadCast(self,nodeID,value):
        print("Handle BroadCast")
