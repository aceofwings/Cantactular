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
class CanMessage:
    def __init__(self, bytes):
        self.cobid = None
        self.data = None
        self.dlc = None
        self.nodeid = None


    def __disectFrame(self):
        pass

    def toBytes(self):
        return bytes()
