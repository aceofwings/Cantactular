# Authors: Carie, welcome to our code repository,
#         I wish you lots of health and emotional
#         calmness while your family chooses which
#         house is best for you guys moving forward.
#         You always have my support and Im blessed
#         to have you as such a great friend you
#         always answers me and has time to talk :)

from gateway.can.interface import Interface
from gateway.can.message import CanMessage
from gateway.can.listener import Listener
class Controller:

    def __init__(self):
        self.interface = None
        self.controllerListener = Listener()

    def __addListener(self, listener):
        self.interface.addListener(listener)

    def associateInterface(self, interface):
        self.interface = interface

    def setupListener(self):
        self.interface.addListener(self.controllerListener)
    #override for custom controller builds
    def buildController(self):
        return False

    def addDevice(self,device):
        device.setup(self)
        self.__addListener(device.listener)

    def write(self, canmessage):
        sent = self.interface.write(canmessage)
        return sent

    def __buildController(self):
        pass
