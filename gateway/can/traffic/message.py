import json
import struct

fstring = b'<IB3x8s'

class CanMessage(object):
    """
    Ultimate object used to transmit data to other applications
    """

    def __init__(self,**kwargs):
        self.__dict__.update(kwargs)

    @property
    def data(self):
        return self.__dict__['data']
    @property
    def canid(self):
        return self.__dict__['canid']
    @property
    def dlc(self):
        return self.__dict__['dlc']
    @property
    def timestamp(self):
        return self.__dict__['received']
    @property
    def type(self):
        return self.__dict__['type']
    @property
    def header(self):
        return self.__dict__['header']
    @property
    def addr(self):
        return self.__dict__['addr']
    @property
    def data_int(self):
        return int.from_bytes(self.data,'big')

    def to_JSON(self):
        """
        Takes Can Packet as list of 16 bytes, the network, type and endian of data
        bytes: list of integers, length should be 16
        CAN Frame: CANID (4) , DataLen (1) , Padding (3) , Data (0 - 8)(Big Endian)
        Returns JSON string that can be encoded
        """

        message = {'canid' : self.canid, 'dlc' : self.dlc, 'received' : self.timestamp, 'type' : self.type}

        if self.dlc == 0:
            message['data'] = [0]
        else:
            print(self.data)
            message['data'] = list(self.data[0: 16 - self.dlc])
        return json.dumps(message)

    @classmethod
    def from_JSON(cls,line):
        """
        Takes the formatted JSON string and convert it to CAN Frame (list of 16 bytes)
        and endian of data.
        Returns a tuple of bytes list,network,type
        """
        message = json.loads(line)
        return CanMessage(**message)


    # TODO: encode message as bytes object
    # def to_bytes(self,line):
    #     """
    #     Takes the formatted JSON string and convert it to CAN Frame (list of 16 bytes)
    #     and endian of data.
    #     Returns a tuple of bytes list,network,type
    #     """
    #     message = json.loads(line)
    #     messagedata = message['message']
    #     fstring = b'<IB3x8s'
    #     can = struct.pack(fstring, messagedata['canid'], messagedata['dlc'], bytes(messagedata['data']))
    #     can = list(can)
    #     can[8:] = (bytes(messagedata['data']))
    #     for i in range(8, 16 - messagedata['dlc']):
    #         can.insert(i, 0)
    #     can = bytes(can)
    #     return can, message['type']
