from gateway.can.controllers.base import BaseController, ControllerContainer
from gateway.can.control.notices import NewConnection
import logging


logger = logging.getLogger(__name__)

class EngineControllerContainer(ControllerContainer):
    def matcher(self,message):
        matches = super().matcher(message)
        matches.append(message['HEADER'])
        return matches

class InternalController(BaseController):

    CC = EngineControllerContainer.getContainer(__name__)
    msg_type = "ENGINE"

    @CC.handler("NEW_CONNECTION")
    def handle_new_connection(engine,message):
        engine.queue_notice(NewConnection(message['app_address']))
