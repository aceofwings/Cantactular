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
from gateway.can.interface import Interface
from gateway.can.message import CanMessage
from gateway.can.listener import Listener
class Controller:

    def __init__(self):
        self.interface = None
        self.controllerListener = Listener()

    def addListener(self, listener):
        self.listeners.append(listener)

    def associateInterface(self, interface):
        self.interface = interface

    def setupListener(self):
        self.interface.addListener(self.controllerListener)
    #override for custom controller builds
    def buildController(self):
        return False

    def write(self, canmessage):
        sent = self.interface.write(canmessage)
        return sent

    def __buildController(self):
        pass



#     ###############################
#     #Accpets parameter for interface device address and creates a new Interface object
#     #Returns the updated list of Interface objects in Controller
#     def addInterface(self, address):

#         try:
#             i = Interface(address, self.listeners)
#         except:
#             pass

#         self.interfaces.append(i)

#         return self.i #only returns interface created

#     ##############################
#     #Starts an Interface, i is index in list of Interfaces, if Not provided, all interfaces are started
#     #Returns True if all interfaces were successfully bound to their addresses, False if one Fails
#     def startInterface(self, i=None):
#         if i is not None:
#             self.interfaces[i].start()
#             return True
#         else:
#             if len(self.interfaces) == 0:
#                 return False
#             for interface in self.interfaces:
#                 success = interface.start()
#                 return success
