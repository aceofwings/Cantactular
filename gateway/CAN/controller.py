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
from interface import Interface
from message import CanMessage

class Controller:

    def __init__(self):
        self.interfaces = []

    ###############################
    #Accpets parameter for interface device address and creates a new Interface object
    #Returns the updated list of Interface objects in Controller
    def addInterface(self, address):

        i = Interface(address)

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


if __name__ == "__main__":

    kicktheCAN = Controller()
    can0 = kicktheCAN.addInterface("vcan0")[0]
    kicktheCAN.startInterface()
    objdic = ObjectDictionary.initialize('../edsfiles/MotorController.eds')

    canmessage = CanMessage.create(2894, b'jdnsje75')

    print("writing: "+str(canmessage))
    sent = can0.write(canmessage)
    print("sent: "+ str(sent))



    for mesg in can0:
        print(mesg)
