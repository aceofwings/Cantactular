from gateway.can.control.matcher import Matcher, CannotMatch
from gateway.can.controllers.base import EVTCAN
from gateway.evtcan.device_construct import DeviceConstruct
from gateway.can.traffic.message import CanMessage

class EvtCanMatcher(Matcher):
    """
    This matcher will take a received can messsage and ultimately match it to a handler or handlers
    The way to match the message, depends on the match_and_handle function.

    EVTCAN is all canid therefore messages or matched
    """
    match_type = EVTCAN
    match = {"*": []}

    def __init__(self):
        self.construct = DeviceConstruct()
        self.database = self.construct.fetchDatabase()
        self.messageBox = self.construct.masterMessageBox()
        super().__init__()


    def setup_quick_match(self):
        """
        convert any handlers with match string type to a canid
        """
        for handler in self.handlers:
            if handler.match in self.match:
                self.match[handler.match].append(handler)
            elif type(handler.match) is str:
                for message in self.database.Messages():
                    if message.Name() == handler.match:
                        self.match.setdefault(message.CANID(),[])
                        self.match[message.CANID()].append[handlers]
            elif type(handler.match) is int:
                self.match.setdefault(handler.match,[])
                self.match[handler.match].append(handler)
            else:
                raise CannotMatch()

    def match_and_handle(self,message):
        """
        Called by the service for a particular message
        """
        for handler in  self.match["*"]:
            if message.canid in self.messageBox:
                handler(message)
                #handler(self.messageBox[message.canid](message.data_int))
        if message.canid in self.match:
            for handler in self.match[message.canid]:
                if message.canid in self.messageBox:
                    handler(self.messageBox[message.canid](message.data_int))
