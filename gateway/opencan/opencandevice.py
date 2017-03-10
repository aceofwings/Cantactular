from gateway.can.device import Device

class MotorControllerDevice(Device):
    def __init__(self, nodeID, controller)
        self.nmt = NMT(nodeID, controller)
        self.listener = Listener()

        self.listener.addHandler(self.nodeID + 0x70, self.nmt.handleheartBeat)
        self.listener.addHandler(self.nodeID + 0x00, self.nmt.handleNMT)

        self.controller.addListener(self.listener)
