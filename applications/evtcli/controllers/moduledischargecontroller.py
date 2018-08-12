from gateway.can.controllers.base import BaseController
from lib.evtcurses import ScreenObject, screenObjects, appendToScreenObjects

class ModuleDischargeController(BaseController):

    discharge_base_text = "Discharge "
    def dicharge_text(self,num):
        return self.discharge_base_text + str(num) + ": "

    def __init__(self):
        print("intializing " , __name__)
        self.discharge = ScreenObject(0,1,"This is my text")

    @BaseController.handleEvt(0x700)
    def discharge(self, message):#required message headers for handles
        message.Module_Discharge_1()
