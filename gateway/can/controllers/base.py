class Controller(object):
    MSG_SEND_SIZE = 16


class ControllerContainer(object):

    controllers = {}
    engine = None

    def __init__(self):
        self.defaultDefinitons = ["*"]
        self._handlers = dict.fromkeys(self.defaultDefinitons, [])


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
        return cls()
    @classmethod
    def setEngine(cls,engine):
        cls.engine = engine



class BaseController(Controller):

    CC = ControllerContainer.getContainer(__name__)

    msg_type="CAN"
    def __init__(self):
        super().__init__()

    def send_to_bus(self,message):
        pass

    def handle_message(self,message):
        self.CC.handle(message)
    #should figure out design to wrap as a debugger
    @CC.handler("*")
    def handle_all(engine,message):
        pass

class EvtCanController(BaseController):

    CC = ControllerContainer.getContainer(__name__)
    msg_type="EVTCAN"

    @CC.handler("*")
    def foward_to_bus(engine,message):
        print(message)


class OpenCanController(BaseController):

    CC = ControllerContainer.getContainer(__name__)
    msg_type="OPENCAN"

    @CC.handler("*")
    def foward_to_bus(engine,message):
        print("message")

class MiscController(BaseController):

    CC = ControllerContainer.getContainer(__name__)
    msg_type="MISC"

    @CC.handler("*")
    def stuff(engine,message):
        print(message)
