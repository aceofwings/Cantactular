
EVTCAN = "EVTCAN"
OPENCAN = "OPENCAN"

class HandlerAssociator(type):
    def __new__(cls, clsname, bases, dct):
        class_frame =  type.__new__(cls, clsname, bases, dct)
        handlers = []
        for attribute in dct.values():
            if(hasattr(attribute,'match')):
                handlers.append(attribute)
        class_frame.handlers = handlers
        return class_frame

class Controller(object,metaclass=HandlerAssociator):
    MSG_SEND_SIZE = 16

    def __init__(self):
        super().__init__()

    def build_controller(self):
        """
        Associate the defined handlers with the instance, return a list
        assocaited handlers for further match definitions
        """
        ctrl_funcs = []
        for handler in self.handlers:
            ctrl_funcs.append(handler.__get__(self))
        return ctrl_funcs



class BaseController(Controller):

    msg_type="CAN"

    def __init__(self):
        super().__init__()

    def send_to_bus(self,message):
        pass

    def handle_message(self,message):
        self.CC.handle(message)
    #should figure out design to wrap as a debugger
    def handler(p):
        def _handle(function):
            function.match = p
            return function
        return _handle

    def handleEvt(messageid = None):
            def _handle(function):
                function.match = (messageid)
                function.type = EVTCAN
                return function
            return _handle

    def handleOpen(index = None, sub = None):
            def _handle(function):
                function.match = (index,sub)
                function.type = OPENCAN
                return function
            return _handle

class EvtCanController(BaseController):

    msg_type="EVTCAN"

    @BaseController.handleEvt(13)
    def handle_me(self,message):
        pass
class OpenCanController(BaseController):

    msg_type="OPENCAN"
    @BaseController.handleOpen(0x1800,0x00)
    def handle_you(self,message):
        pass

class MiscController(BaseController):

    msg_type="MISC"
