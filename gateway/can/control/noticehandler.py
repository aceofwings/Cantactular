

from gateway.can.control import notices


class NoticeContainer(object):

    _noticers = {}

    def __init__(self):
        pass

    def handler(self,p=None):
        def _handle(function):
            self._noticers[p] = function
            return function
        return _handle

    def handle_notice(self,notice):
        self._noticers[notice.__class__](notice)

class NoticeHandler(object):

    NC = NoticeContainer()

    def __init__(self,engine):
        super().__init__()
        self.engine = engine


    @NC.handler(notices.RecoverySucessFull)
    def recoverySucessFull(self,notice):
        print("Hello")
