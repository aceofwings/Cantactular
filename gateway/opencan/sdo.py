#Here will be implemented SDO
import struct
from gateway.utils.objectdictionary import ObjectDictionary
from gateway.can.listener import Listener
from gateway.can.message import CanMessage

class SDO(Listener):
    receivingID = 0x600 #sending request to node
    transmittingID = 0x580 #node response
    sdo_struct = struct.Struct('<BHB')
    command_byte = 0b00101111
    request_timeout = 5 #ms
    num_of_tries = 5

    def __init__(self, device):
        self.nodeID = device.nodeID
        self.controller = device.controller
        self.objectDictionary = ObjectDictionary().initialize(device.edsFile)
        self.addHandler(self.transmittingID+self.nodeID, self._receiveResponse)

    def get(self, handler, index, subindex=None):
        self._sendRequest(______, index, subindex)

    def write(self, handler, data, index, subindex=None):
        self._sendRequest(_______, index, subindex, data)

    def _sendRequest(self, command, index, subindex, data):
        canid = self.receivingID+nodeID
        data = struct.pack('<BHBI', command, index, subindex, data)
        message = CanMessage().create(canid, data)
        self.controller.write(message)

    def _receiveResponse(self, canMessage):

