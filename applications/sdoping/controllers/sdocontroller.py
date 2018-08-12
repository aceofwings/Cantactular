from gateway.can.controllers.base import BaseController
from gateway.can.configuration import Configuration
from gateway.core.service import Service

import socket
import time

class Controller(BaseController):


    def __init__(self):
        print("Starting SDO sender")
        self.interfaces = Configuration.config.interfaces()
        #for interface in self.interfaces:
        #    if self.interfaces[interface] == 'OPENCAN':
        #        self.canif = interface
        self.service = Service(target=Controller.sendSDO,clean_up=self.end)
        self.service.start()
        #

    def sendSDO(running):
        sdoMessages = {
            #index : subindex
            #0x2004 : 0x69,
            0x6068:0x0, #Current
            0x60FF:0x0, #Target Speed
            0x2620:0x0, #Throttle value
            0x2220:0x0, #Throttle input voltage
            0x6077:0x0, #Torque
            0x2721:0x0, #Vehicle Speed
            0x606C:0x0, #Velocity
            0x5000:0x02 #battery Current
        }
        requestID = 0x601
        sock = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
        print("%f : Binding to can1"%(time.time()))
        try:
            sock.bind(("can1",)) #self.canif,))
        except:
            pass
        while not running.isSet():
            canid = list(requestID.to_bytes(4, byteorder='little'))
            for index in sdoMessages:                                   #subindex              #rest of data
                data = canid + [0x08, 0,0,0, 0x40, index&255, index>>8, sdoMessages[index], 0x00, 0x00, 0x00, 0x00]
                try:
                    sock.send(bytearray(data))
#                    print("Sent SDO request to can1")
                except socket.error as err:
                    print("%f : Error Sending SDO request to can1 "%(time.time()), err)
                    time.sleep(0.01)
                #time.sleep(0.05) #50 updates a second

    def end(self):
        print("Ended SDO Controller")
