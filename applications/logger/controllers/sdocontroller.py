from gateway.can.controllers.base import BaseController
from gateway.can.configuration import Configuration
from gateway.core.service import Service

import socket

class Controller(BaseController):


    def __init__(self):
        print("Starting SDO sender")
        #interfaces = Configuration.config.interfaces()
        #print(interfaces)
        self.service = Service(target=Controller.sendSDO,clean_up=self.end)
        self.service.start()
        #

    def sendSDO(running):
        sdoMessages = {
            #index : subindex
            0x2004 : 0x69,
            0x6068:0x0, #Current
            0x60FF:0x0, #Target Speed
            0x2620:0x0, #Throttle value
            0x2220:0x0, #Throttle input voltage
            0x6077:0x0, #Torque
            0x2721:0x0, #Vehicle Speed
            0x606C:0x0, #Velocity
            0x5000:0x02 #battery Current
        }
        requestID = 0x600
        sock = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
        sock.bind(("can0",))
        while not running.isSet():
            canid = list(requestID.to_bytes(4, byteorder='little'))
            for index in sdoMessages:                                   #subindex              #rest of data
                data = canid + [0x04, 0,0,0, 0x40, index&255, index>>8, sdoMessages[index], 0x00, 0x00, 0x00, 0x00]
                sock.send(bytearray(data))
                #might want to pause

    def end(self):
        print("Ended SDO Controller")
