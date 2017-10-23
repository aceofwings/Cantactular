import struct
from gateway.can.message import Message

class SdoMessage(Message):
    self.index = None
    self.subindex = None
    self.dlc = 0
    self.data = None

    def toBytes():
        pass
