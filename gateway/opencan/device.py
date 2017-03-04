from gateway.opencan.nmt import NMT
class CanOpenDevice:
    def __init__(self,nodeID,edsFile=None):
        self.nodeID = nodeID
        self.edsFile = edsFile
        self.controller = None
        self.nmt = None

    #crucial setup of listeners and functions
    def setup(self,controller,listener):
        self.nmt = NMT(self.nodeID,controller)
        self.__buildListener(listener)

    #Define and ad all cruial handlers to the listener.
    #This gets called to add any device specific handlers.
    def __buildListener(listener):
        pass
