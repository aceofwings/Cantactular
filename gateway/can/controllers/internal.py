from gateway.can.controllers.base import BaseController, ControllerContainer
from gateway.can.control.notices import NewConnection

class InternalContainer(ControllerContainer):
    def matcher(self,message):
        matches = self.defaultDefinitons
        matches.append(message['HEADER'])
        return matches

class InternalController(BaseController):

    CC = InternalContainer()

    def __init__(self,engine):
        super().__init__(engine,msg_type="ENGINE")

    @CC.handler("NEW_CONNECTION")
    def handle_new_connection(self,engine,message):
        with engine.client_lock:
            self.applications.append(message['app_address'])
            engine.queue_notice(NewConnection(message['app_address']))
    
