#Authors: (Please put your name here)
#
#
#
# Can Message - a representation of a CAN message consisting of a COB id
# and data
#
# __init__(self,bytes)
# @param bytes -> raw message bytes
# initialize the data and cobid using bytes
# returns None
# __disectFrame(self)
# helper method for disecting the COB_ID and responsible for
# extracting Node_ID and function ID
#Returns None
#
#toBytes(self)
# Pack the COB_ID, DLC, data into a byte representation
#returns the byte representation of the frame
#Note length must equal 16 bytes
#
# 0 1 2 3     4     5 6 7     8 9 10 11 12 13 14 15
#CANID     datalen  padding
import struct
import time
class CanMessage:
    def __init__(self, bytes=None):
        if bytes is not None:
            can_frame = struct.Struct('<IB3x8s')
            self.canid, self.datalen, self.data = can_frame.unpack(bytes)

    def __str__(self):
        return "id:"+str(self.canid)+" datalen: "+str(self.datalen)+" ::data::" + str(self.data)

    @classmethod
    def create(cls, canid, data): #data must be hexidecimal representation of bytes
        msg = CanMessage()
        msg.canid = canid
        msg.data = data
        msg.datalen = len(data)

        return msg
    @classmethod
    def SDOReponse(cls,canid,data):
        sdomsg = SDOReponse()
        sdomsg.data = data
        sdomsg.canid = canid
        return sdomsg
    def bytes(self):
        return struct.pack(b'<IB3x8s', self.canid, len(self.data), self.data)

    def getIDFunction(self):
        pass
    def getIDnode(self):
        pass


class EvtCanMessage(object):

    def __init__(self,signals,data):
        self.signals = signals
        self.data = struct.Struct('<Q').unpack(data)[0]
        self.canid = None
        self.messagedata = {'time': time.time()};


    def contents(self):
        for name, value in self.signals._asdict().items():
            self.messagedata[name] = value(self.data)
        return self.messagedata

    def __str__(self):
        message = ""
        for name, value in self.signals._asdict().items():
            message = message + name +  " " + str(value(self.data)) + ","
        return message

    def __getitem__(self, i):
        return self.signals[i](self.data)

    def __getattr__(self,value):
         return getattr(self.signals, value)(self.data)

class SDOReponse(CanMessage):
    def __init__(self):
        super().__init__()
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self,value):
        self._data = value
        if type(value) is str:
            self._data = bytearray.fromhex(value)
        self.index = self._data[2]*256+self._data[1]
        self.sub = self._data[3]
        self.datalen = len(value)
        value = ""
        for x in range(4, 8):
            value = str(hex(self._data[x]))[2:4] + value
        self.raw = int(value,16)
        self.hexstring = value
