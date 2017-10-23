import struct
from enum import Enum
from gateway.can.message import Message

class CommandByte(Enum):
    UPLOAD = 0x40
    SEND = 0x40
    DOWNLOAD = 0x2B
    RECIEVE = 0x2B

class SdoMessage(Message):
    packer =  struct.Struct("<BHB8s")
    index = 0
    subindex = 0
    dlc = 0
    __data = b'\x00\x00\x00\x00\x00\x00\x00\x00'

    def toBytes(self,messageType):
        return self.packer.pack(messageType.value, self.index, self.subindex, self.__data)

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self,value):
        self.__data = struct.pack('q',value)

    @classmethod
    def toyBytes(cls,messageType,index,subindex,data):
        pass

    @classmethod
    def getMessege(cls,index,subindex,data):
        m = SdoMessage()
        m.index = index
        m.subindex = subindex
        m.data = data
        return m
