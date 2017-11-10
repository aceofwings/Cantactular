

from gateway.can.control import notices
import logging


logger = logging.getLogger(__name__)

class NoticeContainer(object):

    _noticers = {}

    def __init__(self):
        self.engine = None

    def handler(self,p=None):
        def _handle(function):
            self._noticers[p] = function
            return function
        return _handle

    def handle(self,notice):
        self._noticers[notice.__class__](self.engine,notice)

class NoticeHandler(object):

    NC = NoticeContainer()

    def __init__(self,engine):
        super().__init__()
        self.NC.engine = engine


    @NC.handler(notices.RecoverySuccessfull)
    def recoverySucessFull(engine,notice):
        logger.error("A receiver is now seeing traffic")

    def handle_notice(self,notice):
        try:
            self.NC.handle(notice)
        except KeyError as msg:
            print("Cannot handle error")
