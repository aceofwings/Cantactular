import enum
import logging

logger = logging.getLogger(__name__)

class BaseErrorTypes(enum.Enum):
    NON_EXIST_TYPE = 1
    SOCKET_TIMEOUT = 2
    INVALID_FORMAT = 3
    OTHER_ERROR = 4

class ErrorHandler(object):
    """
    Error Message may have a message attribute which will have a parsed
    object message structure. Depending on the error the msg could be different
    """
    engine = None
    def __init__(self,engine,**options):
        self.force_send = options["force_send"]
        self.engine = engine

    def setup(self,error):
        b_error = None
        if type(error) is BaseErrorTypes:
            return error
        elif type(error) is str:
            b_error = BaseErrorTypes[error]
        elif type(error) is int:
            b_error = BaseErrorTypes(error)
        else:
            logger.error("Unknown Error type")

        if hasattr(error,msg):
            b_error.msg = msg

        if hasattr(error, finish):
            b_error.finish = error.finish

        return b_error

    def setup_and_handle(self,error):
        e = self.setup(error)
        self.handle_error(e)
        #
        #add error anaylsis extension here.
        #
        if callable(e.finish):
            finish(e)

    def handle_error(self,error):
    #a message has been appended to the error, read it for more details
    ## A type error occured for some reason, perhaps send the message as can through both sockets
    ## to see if a response may occur
        if error is NON_EXIST_TYPE:
            if hasattr(error,msg):
                logger.error("Could not handle message type " + error.msg['type'])
                if self.force_send:
                    logger.info("Attempting to send message as type CAN")
                    try:
                        error.msg['type'] = "CAN"
                        self.engine.force_send(error.msg)
                    except Exception as msg:
                        logger.error(msg) #a formating issued occur
            else:
                logger.error("Engine has encountered a non-existent message type")

        if error is SOCKET_TIMEOUT:
            if hasattr(error,socket):
                for receiver in self.engine.receivers:
                    if receiver.socket_descriptor is socket and receiver.stopped.isSet():
                        receiver.attempt_recovery()
                        logger.error("the receiver has stopped, due to in inactivity")
                    if receiver.stopped.isSet():
                        self.engine.coreError({message: { error : "SOCKET_DISCONECT" } })
                        logger.error("Failed to start receiver")
            else:
                    for receiver in self.engine.receivers:
                        if receiver.stopped.isSet():
                            receiver.attempt_recovery():
                        if receiver.stopped.isSet():
                            self.engine.coreError({message: { error : "SOCKET_DISCONECT" } })
