from gateway.opencan.nmt import NMT
from gateway.can.listener import Listener
from gateway.evtcan.controller import EvtCanListener


class Device(object):
    def __init__(self):
        self.controller = None
        self.messageBox = None
    def setup(self,controller):
        self.controller = controller

    def __buildListener(self):
        return Listener()


class CanOpenDevice(Device):
    def __init__(self,nodeID,edsFile=None):
        super().__init__()
        self.nodeID = nodeID
        self.edsFile = edsFile
        self.controller = None
        self.nmt = None

    #crucial setup of listeners and functions
    def setup(self,controller):
        self.controller = controller
        self.nmt = NMT(self.nodeID,controller)
        return self.__buildListener()

    #Define and ad all cruial internal handlers to the listener.
    #This gets called to add any device specific handlers.
    def __buildListener(self):
        listener = Listener()
        listener.addHandler(self.nodeID + 0x70, self.nmt.handleheartBeat)
        listener.addHandler(0x00, self.nmt.handleNMT)
        return listener

class EvtCanDevice(Device):
    def __init__(self):
        super().__init__()
        self.messageBox = None

    def setup(self,controller):
        self.controller = controller
        return self.__buildListener()

    def __buildListener(self):
        listener = EvtCanListener(self.messageBox)
        return listener
