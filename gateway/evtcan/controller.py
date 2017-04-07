from  gateway.can.controller import Controller
from gateway.can.listener import Listener
import struct

class EvtCanController(Controller):
    def __init__(self):
        super().__init__()
        self.controllerListener = EvtCanListener()

class EvtCanListener():
    def __init__(self):
        self.boMessages = {}

    def addHandler(self,canDescriptor):
        pass
