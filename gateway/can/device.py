from gateway.canopen.nmt import NMT
from gateway.can.listener import Listener
from gateway.evtcan.evt_listener import EvtCanListener
from gateway.canopen.sdo import SDO

class Device(object):
    def __init__(self):
        self.controller = None
        self.messageBox = None
        self.listener = None

    def setup(self,controller):
        self.controller = controller

    def __buildListener(self):
        self.listener = Listener()
        return self.listener


class CanOpenDevice(Device):
    def __init__(self,nodeID,edsFile=None):
        super().__init__()
        self.nodeID = nodeID
        self.edsFile = edsFile
        self.controller = None
        self.nmt = None
        self.sdo = None

    #crucial setup of listeners and functions
    def setup(self,controller):
        self.controller = controller
        self.nmt = NMT(self.nodeID,controller)
        self.sdo = SDO(self)
        self.controller.interface.addListener(self.sdo)
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
        self.__buildListener()

    def __buildListener(self):
        self.listener = EvtCanListener()
        self.listener.messages = self.messageBox.messages
