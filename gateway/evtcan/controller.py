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
        super().__init__()
        self.messages = messageDescriptor.messages


    def notify(self,canmessage):
        for handler in self.handlers[canmessage.canid]:
            message = EvtCanMessage(self.messages, canmessage.data)
            handler(canmessage.canid, message)
