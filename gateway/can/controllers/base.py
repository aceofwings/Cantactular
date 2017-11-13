class Controller(object):
    MSG_SEND_SIZE = 16

class ControllerContainer(object):

    _handlers = {}

    defaultDefinitons = ["*"]

    def __init__(self):
        self.engine = None

    def handler(self,p=None):
        def _handle(function):
            self._handlers.get(p,[])
            self._handlers.append(function)
            return function
        return _handle

    def handle(self,message):
        """
        handle function called specifically to route messages to correct functions
        """
        matches = self.matcher(message)
        for match in matches:
            for handler in self._handlers[match]:
                handler(self.engine,message)

    def matcher(self,message):
        matches = self.defaultDefinitons
        return matches


class BaseController(Controller):
    CC = ControllerContainer()

    def __init__(self,engine,msg_type="CAN"):
        self.type = msg_type
        self.CC.engine = engine

    def send_to_bus(self,message):
        self.CC.engine.CANsend(message)

    def handle_message(self,message):
        self.CC.handle(message['message'])

    @CC.handler("*")
    def handle_all(self,engine,message):
        self.send_to_bus(message)

class EvtCanController(BaseController):
    def __init__(self,engine):
        super().__init__(engine,msg_type="EVTCAN")

class OpenCanController(BaseController):
    def __init__(self,engine):
        super().__init__(engine,msg_type="OPENCAN")


class MiscController(BaseController):
    def __init__(self,engine):
        super().__init__(engine,msg_type="MISC")

    @CC.handler("*")
    def stuff(self,engine,message):
        print(message)
