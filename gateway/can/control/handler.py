
import enum
from gateway.can.control.errorhandler import BaseErrorTypes

"""
Base handle
"""
class BaseMessageTypes(enum.Enum):
    """
    Default types of messages expected by the handler. This can be overridden with
    a new handler to allow for more types of messages to come through the bus.
    """
    EVTCAN = 1
    OPENCAN = 2
    ERROR = 3

class BasicMessageHandler(object):
    """
    logic for handling messages. Abstracted to allow for easy customization.
    Override
    """
    engine = None

    def __init__(self,engine, mts_enum=None):
        super().__init__()
        self.engine = engine

        if mts_enum is not None:
            self.mts = mts_enum
        else:
            self.mts = BaseMessageTypes

    def _msg_type_compose(self,msg_type):
        """
        takes a raw string or int and turns it into a comparable enum
        """
        if type(msg_type) is str:
            return self.mts[msg_type]
        elif type(msg_type) is int:
            return self.mts(msg_type)

    def setup_and_handle(self,msg_type,message):
        try:
            self.handle(self._msg_type_compose(msg_type),message)
        except KeyError as msg:
            error = BaseErrorTypes.NON_EXIST_TYPE
            error.msg = message
            self.engine.queue_error(error)

    def handle(self,e_type,message):
        if e_type is BaseMessageTypes.EVTCAN:
            print("EVTCAN")
        elif e_type is BaseMessageTypes.OPENCAN:
            print("OPENCAN")
        elif e_type is BaseMessageTypes.ERROR:
            print("ERROR")

    def handle_error(self):
        pass
