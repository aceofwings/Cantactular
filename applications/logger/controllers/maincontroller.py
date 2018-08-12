from gateway.can.controllers.base import BaseController
from gateway.core.service import Service
from gateway.utils.logger import logger, loadLogger
import time

class MainController(BaseController):

    def __init__(self):
        print("intializing Logging Application")
        loadLogger()
        #self.service = Service(target=self.time_count,clean_up=self.end)
        #self.service.start()
        #self.count = 0

    @BaseController.handleEvt("*")
    def handleAllEVT(self,message):
        logger.debug("%f, %s, %04X # %02X %02X %02X %02X %02X %02X %02X %02X"%(message.timestamp,message.type,message.canid,*message.data))
        #self.count += 1
        #print(count)

    @BaseController.handleOpen("*")
    def handleAllOPEN(self,message):
        logger.debug("%f, %s, %04X # %02X %02X %02X %02X %02X %02X %02X %02X"%(message.timestamp,message.type,message.canid,*message.data))
        #self.count += 1

    #def time_count(self,running):
        #t = time.time()
        #while not running.isSet():
            #s = time.time()
            #print(s)
            #if((s - t) >= 1):
                #t = s
                #print("%i messages per second"%(self.count))
                #self.count = 0


    def end(self):
        print("Ended Log counter")
