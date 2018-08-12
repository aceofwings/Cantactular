from gateway.can.controllers.base import BaseController
from lib.evtcurses import ScreenObject, screenObjects, appendToScreenObjects

class CellTempController(BaseController):
    numberOfCells = 30
    objects = []

    def __init__(self):
        print("intializing " , __name__)
        columnTitle =  ScreenObject(22,1, "Cell Temperatures")
        columnTitle.data = "(C)"
        columnTitle.colorPair = 22
        for i in range(0,self.numberOfCells):
            self.objects.append(ScreenObject(22,i + 2, "Cell Temp " + str(i) + " "))
            screenObjects.append(self.objects[i])
        screenObjects.append(columnTitle)
    @BaseController.handleEvt(129)
    def handleBMSCellTemp(self,message):
        cellNumber0, cellNumber1  = message.Cell_no0(), message.Cell_no1()
        cellTemp0, cellTemp1 = message.Cell_temperature0(), message.Cell_temperature1()
        if len(self.objects) > cellNumber0 and len(self.objects)  > cellNumber1:
            self.objects[cellNumber0].data = cellTemp0
            self.objects[cellNumber1].data = cellTemp1
