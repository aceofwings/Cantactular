
import struct
#NMT
##
#HeartBeat States are broadcasted with a node id of 0x70 + deviceID
#Data field with have 1 byte of data
##
heartBeatStates ={
'bootup' : 0x00,
'stopped' : 0x04,
'operational':0x05,
'preoperational': 0x7f
}

##
#these states are broadcasted in order set a device into a certain states
#CAN IDS will be broadcast(0x00) and will have 2 bytes of data
##
states = {
'operational': 0x01,
'stop': 0x02,
'preoperational':0x80,
'reset' :0x81 ,
'resetcom' : 0x82
}
#Some cases we are not responsible for setting state and a device may want to change
#state. We retrieve the information by heartbeat but will want to translate to
#device state
heartBeatToState = {
0x00 :'preoperational',
0x04 :'stop',
0x05 :'operational',
0x7f : 'preoperational',
}
class NMT(object):
    #@params controller for sending and recieving messages for NMT
    #        deviceID the device ID for the nmt to use to send messages
    def __init__(self,deviceID,controller):
        self.controller = controller
        self.deviceID = deviceID
        self.__state = None

    @property
    def state(self):
        return self.__state

    @state.setter
    def setState(self, value):
        if value in states:
            data = self.nodeID + states[value]
            self.controller.sendMessage(0x00,data)

#handle CAN IDs of 0x70 + nodeID
    def handleheartBeat(self,nodeID,data):
        stateCode = struct.unpack('B',data)
        if heartBeatToState[stateCode] == self.__state:
            self.__state = heartBeatToState[stateCode]
            #TODO forward statechange event
#Handle a the nodes broadcasted Date.
    def handleNMT(self,nodeID, data):
        deviceID, state  = struct.unpack('BB',data)
