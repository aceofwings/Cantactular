
"""
Base handle
"""
class MessageTypes(enum.Enum):
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
    mts = MessageTypes()

    def __init__(self,engine, mts_enum=None):
        super().__init__()
        self.engine = engine

        if mts_enum is not None:
            mts = mts_enum()

    def _msg_type_compose(self,msg_type):
        """
        takes a raw string or int and turns it into a comparable enum
        """
        if type(msg_type) is str:
            return MessageTypes[msg_type]
        elif type(msg_type) is int:
            return MessageTypes(msg_type)

    def setup_and_handle(self,msg_type,message):
        self.handle(self._msg_type_compose(msg_type),message)

    def handle(self,e_type,message):
        if e_type is MessageTypes.EVTCAN:
            print("EVTCAN")
        elif e_type is MessageTypes.OPENCAN:
            print("OPENCAN")
        elif e_type is MessageTypes.ERROR:
            print("ERROR")
