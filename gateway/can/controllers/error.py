from gateway.can.controllers.base import BaseController


class ErrorController(BaseController):

    #CC = BaseController.ControllerContainer()

    def __init__(self,engine):
        super().__init__(engine,msg_type="ERROR")
