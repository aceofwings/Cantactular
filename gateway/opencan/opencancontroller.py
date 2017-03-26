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
        if self.interface is None:
            pass # try to fetch interface, or lazy load
        else:
            self.interface.addListener(listener)

    def addDevice(self,device):
        device.controller = self
        deviceListener = device.setup()
        self.__addListener(deviceListener)
    #associate a device with the controller

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
        for handler in handlers[canmessage.canid]:
            handler(canmessage.canid,canmessage.data)
