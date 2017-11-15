from gateway.can.controllers.base import BaseController, ControllerContainer
from gateway.can.control.notices import NewConnection

class InternalController(BaseController):

    CC = ControllerContainer.getContainer(__name__)
    msg_type = "ENGINE"

    @CC.handler("NEW_CONNECTION")
    def handle_new_connection(self,engine,message):
        print(engine)
        with engine.client_lock:
            self.applications.append(message['app_address'])
            engine.queue_notice(NewConnection(message['app_address']))
