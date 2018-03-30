

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
    """
    The Notice handler which can be overriden for additional functionality, reponds and changes state and execution of the engine based on the notices recieved.
    Some notices may just be warnings, while others may follow with the engine fowarding to its clients about state change.
    """

    NC = NoticeContainer()

    def __init__(self,engine):
        super().__init__()
        self.NC.engine = engine


    @NC.handler(notices.RecoverySuccessfull)
    def recoverySucessFull(engine,notice):
        logger.error("A receiver is now seeing traffic")

    @NC.handler(notices.NewConnection)
    def handleNewConnection(engine,notice):
        with engine.client_lock:
            logger.error("A new application has connected " + notice.addr)
            if engine.max_connections is None:
                engine.applications.append(notice.addr)
            elif engine.max_connections > len(engine.applications):
                engine.applications.append(notice.addr)
            else:
                pass
                #deny request



    def handle_notice(self,notice):
        try:
            self.NC.handle(notice)
        except KeyError as msg:
            print("Cannot handle error")
