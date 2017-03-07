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

#MotorController Listener
#handlers are functions ready to recieve data and the canid
class MotorControllerListener(Listener):
    handlers = {}
    def addHandler(canid, handler):
        if canid in handlers:
            handlers[canid].append(handler)
        else:
            handlers[canid] = []
            handlers[candid].append(handler)

    def removeHandler(canid,handler):
        pass
    def notify(self,canmessage):
        for handler in handlers[canmessage.canid]
            handler(canmessage.canid,canmessage.data)
