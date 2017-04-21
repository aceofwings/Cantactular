#Here will be implemented SDO
import struct
from gateway.utils.objectdictionary import ObjectDictionary
from gateway.can.listener import Listener
from gateway.can.message import CanMessage

class SDO(Listener):
    receivingID = 0x600 #sending request to node
    transmittingID = 0x580 #node response
    r_write_command = 0x20
    t_write_command = 0x60
    read_command = 0x40
    sdo_struct = struct.Struct('>BH5B')
    request_timeout = 5 #ms
    num_of_tries = 5

    def __init__(self, device):
        self.nodeID = device.nodeID
        self.controller = device.controller
        self.objectDictionary = ObjectDictionary().initialize(device.edsFile)
        self.addHandler(self.transmittingID+self.nodeID, self._receiveResponse)
        self.notifyhandlers = {}

    def read(self, handler, index, subindex=0x0):
        canid = self.receivingID + self.nodeID
        d = [self.read_command, index&255, index>>8, subindex, 0x00, 0x00, 0x00, 0x00]
        data = ''.join('%02x' % x for x in d)
        response = (index&255)**16 + (index>>8)**8 + subindex
        self.notifyhandlers[response].append(handler)

    def write(self, handler, data, index, subindex=0x0):
        self._sendRequest(_______, index, subindex, data)

    def _sendRequest(self, index, subindex):
        pass


    def _receiveResponse(self, canMessage):
        pass
