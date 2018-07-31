from gateway.can.controllers.base import BaseController
from gateway.core.service import Service
from gateway.utils.logger import logger, loadLogger


class MainController(BaseController):

    def __init__(self):
        print("intializing Logging Application")
        loadLogger()

    @BaseController.handleEvt("*")
    def handleAllEVT(self,message):
        logger.debug("%f, %s, %04X # %02X %02X %02X %02X %02X %02X %02X %02X"%(message.timestamp,message.type,message.canid,*message.data))

    @BaseController.handleOpen("*")
    def handleAllOPEN(self,message):
        logger.debug("%f, %s, %04X # %02X %02X %02X %02X %02X %02X %02X %02X"%(message.timestamp,message.type,message.canid,*message.data))
