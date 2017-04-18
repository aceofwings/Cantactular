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
        msg.data = bytearray.fromhex(data)
        msg.datalen = len(data)

        return msg

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


    def cotents(self):
        messagedata= {}
        for name, value in self.signals._asdict().items():
            messagedata[name] = value(self.data)
        print(messagedata)
    def __getitem__(self, i):
        return self.signals[i](self.data)

    def __getattr__(self,value):
         return getattr(self.signals, value)(self.data)
