import enum
import logging
import gateway.can.control.errors as errors

logger = logging.getLogger(__name__)

class ErrorHandler(object):
    """
    Error Message may have a message attribute which will have a parsed
    object message structure. Depending on the error the msg could be different
    """
    engine = None


    def __init__(self,engine, **options):
        self.force_send = options["force_send"]
        self.engine = engine

    def setup(self,error):
        if isinstance(error, errors.EngineError):
            return error
        else:
            logger.error("Unknown Error has occured")
            raise error


    def setup_and_handle(self,error):
        e = self.setup(error)
        self.handle_error(e)
        #
        #add error anaylsis extension here.
        #
        e.finish()

    def handle_error(self,error):
        """
        Handle an error from the engine. To see how the engine
        """
        try:
            raise error
            logger.info("An Engine error has risen")
        except errors.NonExtistentType as NT:
                logger.error("Could not handle message type " + error.msg['type'])
                if self.force_send:
                    logger.warning("Attempting to send message as type CAN")
                    try:
                        error.msg['type'] = "CAN"
                        self.engine.force_send(error.msg)
                    except Exception as msg:
                        logger.error(msg) #a formating issued occur
        except errors.InvalidMessageFormat as IM:
            logger.error("Invalid message format")
            self.engine.coreError({message: {error : "INVALID_MESSAGE_FORMAT"}})
        except errors.CanSocketTimeout as CT:
            for receiver in self.engine.receivers:
                if receiver.socket_descriptor is CT.socket and receiver.stopped.isSet():
                    receiver.attempt_recovery()
                    logger.error("the receiver has stopped, due to in inactivity")
                if receiver.stopped.isSet():
                    self.engine.coreError({message: { error : "SOCKET_DISCONECT" } })
                    logger.error("Failed to start receiver")
