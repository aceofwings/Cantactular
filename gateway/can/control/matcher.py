from gateway.can.controllers.base import OPENCAN
from gateway.can.traffic.message import CanMessage
from gateway.can.control.notices import NewConnection
###Matcher Constants###
ALL = "*"

class Matcher(object):
    """
    Responsible for matching messages with their respected handlers.
    Depending on the protocol the matcher will translate the message.

    """
    defaultDefinitons = []
    handlers = []
    match_type = "CAN"

    def __init__(self):
        self.setup_quick_match()


    def get_type(message):
        return message['type']

    def toCanMessage(message):
        return CanMessage.from_JSON(message)

    def setup_quick_match(self):
        """
        do any matcher setup up in here
        """
        pass

    def match_and_handle(self,message):
        """
        Ultimately called by the service to handle a Can Message .
        the can message will then be formatted or passed along based on the implementation
        of match and handle
        """
        pass

class OpenCanMatcher(Matcher):
    match_type = OPENCAN

class InternalMatcher(Matcher):

    match_type = "ENGINE"

    def __init__(self,engine):
        self.engine = engine
        self.handlers = {"NEWCONNECTION" : self.handle_new_connection}

    def match_and_handle(self,message):
        self.handlers[message.header](message)

    def handle_new_connection(self,message):
        self.engine.queue_notice(NewConnection(message.addr))


class CannotMatch(Exception):
    pass
