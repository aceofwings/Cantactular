from gateway.can.controllers.base import BaseController, ControllerContainer


class ErrorContainer(ControllerContainer):
    def matcher(self,message):
        matches = self.defaultDefinitons
        matches.append(message['HEADER'])
        return matches


class ErrorController(BaseController):

    CC = ErrorContainer()

    def __init__(self,engine):
        super().__init__(engine,msg_type="ERROR")
