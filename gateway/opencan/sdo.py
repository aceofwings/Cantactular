#Here will be implemented SDO
import struct
import sys
from gateway.utils.objectdictionary import ObjectDictionary
from gateway.can.listener import Listener
from gateway.can.message import SDOReponse,CanMessage
from gateway.opencan.sdologger import SDOLog

class SDO(Listener):
    receivingID = 0x600 #sending request to node
    transmittingID = 0x580 #node response
    r_write_command = 0x20
    t_write_command = 0x60
    read_command = 0x40

    write_values = {0x2220:0x0}
    write_times = 0

#sdo_struct = struct.Struct('>BH5B')
#request_timeout = 5 #ms
#num_of_tries = 5
#print( str(canid)+': '+str(index)+' '+str(subindex) )
#print( "["+str(hex(canid)) +"] "+ str(data) )
#print(str(data&255)+': '+bin(data)+hex(data))
    def __init__(self, device):
        super().__init__()
        self.device = device
        self.nodeID = device.nodeID
        self.controller = device.controller
        self.objectDictionary = ObjectDictionary.initialize(device.edsFile)
        self.addHandler(self.transmittingID+self.nodeID, self._receiveResponse)
        self.notifyhandlers = {}
        self.log = SDOLog(self)

    def read(self, handler, index, subindex=0x0):
        canid = self.receivingID + self.nodeID
        d = [self.read_command, index&255, index>>8, subindex, 0x00, 0x00, 0x00, 0x00]
        data = ''.join('%02x' % x for x in d)
        address = (index&255)**8 + (index>>8)**16 + subindex
        self.notifyhandlers[address] = handler
        message = CanMessage.SDOReponse(canid, data)
        self.controller.write(message)

    def write(self, handler, data, index, subindex=0x0):
        canid = self.receivingID + self.nodeID
        d = [self.r_write_command, index&255, index>>8, subindex]
        n = 0
        for i in range(0,4):
            x = data>>(i*8)&255
            d.append(x)
            if x == 0: n+=1
        d[0] += (n<<2)+3
        data = ''.join('%02x' % x for x in d)
        address = (index&255)**8 + (index>>8)**16 + subindex
        self.notifyhandlers[address] = handler
        message = CanMessage.SDOReponse(canid, data)
        self.controller.write(message)

    def _receiveResponse(self, **kwargs):
        print("Care")
        message = CanMessage.SDOReponse(kwargs['message'].canid, kwargs['message'].data)
        if message.canid>>4 == self.transmittingID>>4 :
            cmdbyte = message.data[0]
            address = message.data[2]**16+message.data[1]**8+message.data[3]
            try:
                self.notifyhandlers[address](message)#''.join('%02x'%x for x in message.data[4:8]))
            except KeyError:
                print('SDOError!! received index:sub pair incorrectly? ['+str(hex(message.data[2]*256+message.data[1]))+']['+str(hex(message.data[3]))+']')
        else:
            print('received response that did not match proper canid:: expected 0x580+nodid')
