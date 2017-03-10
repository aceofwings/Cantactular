from gateway.can.controller import Controller
from gateway.can.listener import Listener
#
#CanOpen Controller. responsible for all communication based on the CanOpen
#protocol and contains only devices implemented with the protocol.
#
#
class OpenCanController(Controller):

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

    def __removeDevice(device):
        pass


