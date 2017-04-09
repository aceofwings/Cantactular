from gateway.can.controller import Controller
from gateway.can.listener import Listener
from gateway.can.message import EvtCanMessage
import struct

class EvtCanController(Controller):
    def __init__(self):
        super().__init__()
        self.controllerListener = Listener()


class EvtCanListener(Listener):
    def __init__(self,messageDescriptor):
        super.__init__()
        self.messageDescriptor = messageDescriptor

    def notify(self,canmessage):
        message = EvtCanMessage(self.messageDescriptor[canmessage.canid],canmessage.data)
        for handler in self.handlers[canmessage.canid]:
            handler(canmessage.canid, message)
