# Authors: (Please put your name)
#
#
#
#
#
#
#
#
from gateway.can.interface import Interface

class Controller:

    def __init__(self):
        self.interface = None
        self.listeners = []

    def addListener(self, listener):
        self.listeners.append(listener)

    def createInterface(self, deviceAddress):
        self.interface = Interface(deviceAddress, self.listeners)
        self.interface.start()

    def write(self, canmessage):
        sent = self.interface.write(canmessage)
        return sent
