# Authors: (Please put your name)
#
#
#
#
#
#
#
#
from gateway.utils.objectdictionary import ObjectDictionary
from gateway.CAN.interface import Interface
from gateway.CAN.message import CanMessage

class Controller:

    def __init__(self):
        self.interfaces = []
        self.listeners = []

    def addListener(self, listener):
        self.listeners.append(listener)

    ###############################
    #Accpets parameter for interface device address and creates a new Interface object
    #Returns the updated list of Interface objects in Controller
    def addInterface(self, address):

        i = Interface(address, self.listeners)

        self.interfaces.append(i)

        return self.interfaces

    ##############################
    #Starts an Interface, i is index in list of Interfaces, if Not provided, all interfaces are started
    #Returns True if all interfaces were successfully bound to their addresses, False if one Fails
    def startInterface(self, i=None):
        if i is not None:
            self.interfaces[i].start()
            return True
        else:
            if len(self.interfaces) == 0:
                return False
            for interface in self.interfaces:
                success = interface.start()
                if success == False:
                    return False
