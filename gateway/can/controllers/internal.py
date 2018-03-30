from gateway.can.controllers.base import BaseController
from gateway.can.control.notices import NewConnection
import logging


logger = logging.getLogger(__name__)

class InternalController(BaseController):

    msg_type = "ENGINE"

    def handle_new_connection(message):
        engine.queue_notice(NewConnection(message.addr))
