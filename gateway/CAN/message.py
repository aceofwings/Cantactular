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
            can_frame = struct.Struct('IB3x8B')
            self.indata = can_frame.unpack(bytes)

            self.canid = self.indata[0]
            self.datalen = self.indata[1]

            self.data = self.indata[2:10]


    def __str__(self):
        return "id:"+str(hex(self.canid))+" datalen: "+hex(self.datalen)+" ::data::" + str(self.data)

    def create(canid, data):
        msg = CanMessage()
        msg.canid = canid
        msg.data = data
        msg.datalen = len(data)
        return msg

    def bytes(self):
        return struct.pack(b'IB3x8B', self.canid, self.datalen, self.data[0], self.data[1], self.data[2], self.data[3], self.data[4], self.data[5], self.data[6], self.data[7])



#if __name__ == "__main__":
#    canmess = CanMessage(b'0000000010000000')
#    print(canmess)
