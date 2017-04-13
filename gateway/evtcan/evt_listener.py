from gateway.can.listener import Listener
from gateway.can.message import EvtCanMessage

class EvtCanListener(Listener):
    def __init__(self):
        super().__init__()
        self.messages = {}

#TODO arguments of handlers are going to be KWARGS

    def notify(self,canmessage):
        for handler in self.handlers[canmessage.canid]:
            message = EvtCanMessage(self.messages[canmessage.canid], canmessage.data)
            handler(canmessage.canid, message)


    def notifyAll(self,canmessage):
        if canmessage.canid in self.messages:
            message = EvtCanMessage(self.messages[canmessage.canid], canmessage.data)
            super().notifyAll(message)
