#NMT


states = {
'start': 0x01,
'stop': 0x02,
'preoperation':0x80 ,
'reset' 0x81: ,
'resetcom' 0x82:
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
        return self.state

    @state.setter
    def setState(self, value):
        if value in states:
            data = self.nodeID + states[value]
            self.controller.sendMessage(0x00,data)

    def handleNMT(self,nodeID, data):
        ##TODO unpack data into NMT Format
        pass
