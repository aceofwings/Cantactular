import enum
import logging
import gateway.can.control.errors as errors

logger = logging.getLogger(__name__)

class ErrorHandler(object):
    """
    The error handler is responsible for handling all errors risen within the engine and child threads.
    Based on the type of error, the engine will react, change state and executution.
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
            self.engine.COREerror( {'error' : "INVALID_MESSAGE_FORMAT"})
        except errors.CanSocketTimeout as CT:
            for receiver in self.engine.receivers:
                if receiver.socket_descriptor is CT.socket:
                    receiver.attempt_recovery()
                    logger.error("the receiver has stopped, due to in inactivity -  attempting recovery")
                    if receiver._stop.isSet():
                        self.engine.COREerror({ 'error' : "SOCKET_DISCONECT" })
        except errors.RecoveryTimeout as RT:
                    for receiver in self.engine.receivers:
                        if receiver.socket_descriptor is RT.socket:
                            logger.error("Failed to recover receiver")
                            #log failure of socket and receiver type
        except errors.NonExistentInterface as error:
                print("Interface: " + error.address + " does not exist")
                self.engine.shutdown()
