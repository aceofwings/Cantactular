from gateway.can.controllers.base import BaseController
from gateway.core.service import Service
from lib.evtcurses import ScreenObject, screenObjects, appendToScreenObjects

class IMUController(BaseController):
    def __init__(self):
        print("intializing " , __name__)
        self.columnTitle =  ScreenObject(66, 1, "IMU DATA")
        self.columnTitle.data = ""
        self.columnTitle.colorPair = 22

        self.linearx = ScreenObject(66,2,"Linear X : ")
        self.lineary = ScreenObject(66,3,"Linear Y : ")
        self.linearz = ScreenObject(66,4,"Linear Z : ")
        self.gravityx = ScreenObject(66,5,"Gravity X : ")
        self.gravityy = ScreenObject(66,6,"Grivty Y : ")
        self.gravityz = ScreenObject(66,7,"Grivty Z : ")

        screenObjects.append(self.columnTitle)
        screenObjects.append(self.linearx)
        screenObjects.append(self.lineary)
        screenObjects.append(self.linearz)
        screenObjects.append(self.gravityx)
        screenObjects.append(self.gravityy)
        screenObjects.append(self.gravityz)
        


    @BaseController.handleEvt(512)
    def IMU_linear_acceleration(self,message):
        print("LINEAR")
#        "m/s^2"
        self.linearx.data = message.X_acceleration()
        self.lineary.data = message.Y_acceleration()
        self.linearz.data = message.Z_acceleration()
    @BaseController.handleEvt(513)
    def IMU_gravity_vector(self,message):
#        "m/s^2"
        print("GRAVITY")
        self.gravityx.data = message.X_acceleration()
        self.gravityy.data = message.Y_acceleration()
        self.gravityz.data = message.Z_acceleration()
    @BaseController.handleEvt(514)
    def IMU_quaternion_position(self,message):
        print("QUAD")
#        "quatern"
        message.W_position()
        message.X_position()
        message.Y_position()
        message.Z_position()
