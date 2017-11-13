class Controller(object):
    MSG_SEND_SIZE = 16


class ControllerContainer(object):

    engine = None
    controllers = {}

    def __init__(self,engine):
        self._handlers = {}
        self.defaultDefinitons = ["*"]
        self.engine = engine
    def handler(self,p=None):
        def _handle(function):
            if p not in self._handlers:
                self._handlers.setdefault(p, [])
            self._handlers[p].append(function)
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

    @classmethod
    def getContainer(cls,controller_name):
        print(cls.controllers)
        cls.controllers[controller_name] = cls(cls.engine)
        return cls.controllers[controller_name]

class BaseController(Controller):

    CC = ControllerContainer.getContainer(__name__)

    def __init__(self,engine,msg_type="CAN"):
        self.type = msg_type

    def send_to_bus(self,message):
        self.CC.engine.CANsend(message)

    def handle_message(self,message):
        self.CC.handle(message['message'])


    #should figure out design to wrap as a debugger
    @CC.handler("*")
    def handle_all(engine,message):
        pass

class EvtCanController(BaseController):

    CC = ControllerContainer.getContainer(__name__)

    def __init__(self,engine):
        super().__init__(engine,msg_type="EVTCAN")

    @CC.handler("*")
    def foward_to_bus(engine,message):
        pass#engine.CANsend(message)


class OpenCanController(BaseController):

    CC = ControllerContainer.getContainer(__name__)

    def __init__(self,engine):
        super().__init__(engine,msg_type="OPENCAN")

    @CC.handler("wow")
    def foward_to_bus(engine,message):
        print("hello")
        #engine.CANsend(message)

class MiscController(BaseController):

    CC = ControllerContainer.getContainer(__name__)

    def __init__(self,engine):
        super().__init__(engine,msg_type="MISC")
    @CC.handler("*")
    def stuff(engine,message):
        print(message)
