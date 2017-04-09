from gateway.can.controller import Controller
from gateway.can.listener import Listener

#
#CanOpen Controller. responsible for all communication based on the CanOpen
#protocol and contains only devices implemented with the protocol.
#
#
class CanOpenController(Controller):

    def __init__(self):
        super().__init__()
        self.controllerListener = Listener()


    def sendMessage(self,canID, data):
        pass


    def setupListener(self):
        self.interface.addListener(self.controllerListener)

    def __addListener(self,listener):
        if self.interface  is None:
            pass # try to fetch interface, or lazy load
        else:
            self.interface.addListener(listener)

    def addDevice(self,device):
        deviceListener = device.setup(self)
        self.__addListener(deviceListener)

    def buildController(self):
        self.setupListener()
        return False
    #associate a device with the controller

#MotorController Listener
#handlers are functions ready to recieve data and the canid
class MotorControllerListener(Listener):
    pass
