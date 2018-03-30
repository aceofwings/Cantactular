from gateway.core.provider import Provider
from gateway.evtcan.matcher import EvtCanMatcher
from gateway.can.control.matcher import InternalMatcher


class Server(Provider):

    def __init__(self,engine):
        super().__init__()
        self.engine = engine
        self.matchers = {EvtCanMatcher.match_type : EvtCanMatcher(),InternalMatcher.match_type : InternalMatcher(self.engine)}

    def handleMessage(self,message):
        self.matchers[message.type].match_and_handle(message)
