

from gateway.can.control import notices

class NoticeHandler(object):

    engine = None
    _noticers = {}

    def __init__(self,engine):
        self.engine = engine

    def handler(p=None):
        def _handle(function):
            def wrapper(*args,**kwargs):
                handlerInstance = args[0]
                handlerInstance._noticers[p] = function
                return function
            return wrapper
        return _handle


    def handle_notice(self,notice):
        self._noticers[notice.__class__](notice)

    @handler(notices.RecoverySucessFull)
    def recoverySucessFull(self,notice):
        print("Hello")
