from  gateway.can.controller import Controller
from gateway.can.listener import Listener
import struct

class EvtCanController(Controller):
    def __init__(self):
        super().__init__()
        self.controllerListener = EvtCanListener()





class EvtCanMessage(object):

    def __init__(self,signals,data):
        self.signals = signals
        self.data = struct.Struct('<Q').unpack(data)[0]

    def __getattr__(self,value):
         return getattr(self.signals, value)(self.data)

class EvtCanListener():
    def __init__(self):
        self.boMessages = {}

    def addHandler(self,canDescriptor):
        pass
