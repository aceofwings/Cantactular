from gateway.opencan.nmt import NMT

class Device:

    def __init__(self,nodeID, controller):
        self.nodeID = nodeID
        self.controller = controller
        self.faultbase = FaultBase()
