from gateway.can.controller import Controller
from gateway.can.listener import Listener
#
#CanOpen Controller. responsible for all communication based on the CanOpen
#protocol and contains only devices implemented with the protocol.
#
#
class CanOpenController(Controller):

    def __init__(self):
        self.devices = []

    def __intializeDevice():
        pass

    def sendMessage(self,canID, data):
        pass
    #associate a device with the controller
    def addDevice(self,device,listener):
        self.devices.append(device)
        self.addListener(listener)
        device.setup(self,listener)

    def __removeDevice(device):
        pass

class MotorControllerListener(Listener):
    handlers = []
    def addHandler(canid, handler):
        pass
    def removeHandler(canid,handler):
        pass
    def notify(self,canmessage):
        for handler in handlers[canmessage.canid]
            handler(canmessage)
