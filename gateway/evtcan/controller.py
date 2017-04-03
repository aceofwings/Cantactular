from  gateway.can.controller import Controller

class EvtCanController(Controller):
    def __init__(self):
        super().__init__()
        self.controllerListener = Listener()
