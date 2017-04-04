from  gateway.can.controller import Controller
from gateway.can.listener import Listener
class EvtCanController(Controller):
    def __init__(self):
        super().__init__()
        self.controllerListener = EvtCanListener()





class EvtCanMessage(object):

    def __init__():
        self.messageDescriptor = None
        self.signals = None

    def buildSignals():
        pass



class EvtCanListener():
    def __init__(self):
        self.boMessages = {}

    def addHandler(self,canDescriptor):
        pass
