from gateway.core.provider import Provider
from gateway.evtcan.matcher import EvtCanMatcher
from gateway.can.controllers.error import ErrorController
from gateway.can.controllers.internal import InternalController

class Application(Provider):

    def __init__(self,engine):
        super().__init__()
        self.engine = engine
        self.matchers = {EvtCanMatcher.match_type : EvtCanMatcher()}

    def handleMessage(self,message):
        self.matchers[message.type].match_and_handle(message)
