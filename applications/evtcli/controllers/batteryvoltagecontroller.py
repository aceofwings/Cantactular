
from gateway.can.controllers.base import BaseController
from lib.evtcurses import ScreenObject, screenObjects, appendToScreenObjects

class BattteryVoltageController(BaseController):

    numberOfCells = 30
    objects = []

    def __init__(self):

        self.packageVoltage =  ScreenObject(45, 1, "PackVoltage")
        self.packageVoltage.colorPair = 22
        self.pvoltage = ScreenObject(45,2,"Value : ")
        self.packageVoltage.data = ("(mV)")
        self.pvoltage.colorPair = 197

        columnTitle =  ScreenObject(0,1, "Cell Voltages")
        columnTitle.data = "(mV)"
        columnTitle.colorPair = 22
        for i in range(self.numberOfCells):
            self.objects.append(ScreenObject(0,i + 2, "Cell Voltage " + str(i) + " "))
            screenObjects.append(self.objects[i])
        screenObjects.append(columnTitle)
        screenObjects.append(self.pvoltage)
        screenObjects.append(self.packageVoltage)

    @BaseController.handleEvt(128)
    def handleBMSCellVoltage(self,message):
        cellNumber0, cellNumber1  = message.Cell_no0(), message.Cell_no1()
        cellVoltage0, cellVoltage1 = message.Cell_voltage0(), message.Cell_voltage1()
#        print(cellNumber0,cellVoltage0,cellNumber1,cellVoltage1)
#        if len(self.objects) > cellNumber0 and len(self.objects)  > cellNumber1:
        self.objects[cellNumber0-12].data = cellVoltage0
        self.objects[cellNumber1-12].data = cellVoltage1


    @BaseController.handleEvt(131)
    def handlePackVoltage(self,message):
        self.pvoltage.data = message.Pack_voltage()



# cansend vcan0 080#
