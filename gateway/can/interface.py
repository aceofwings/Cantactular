#Authors: Nicholas Amatruda
#
#
#Interface defines a virtual representation of the physical can interface
#These interfaces usually are defined by a CANIP or NIC name, eg CAN0
#
#
#controller = Reference to Gateway Controller that Interface belongs to
#device = Reference to network device on computer for interface to read and write to
#
#
#launchNotifer(self):
#Launches a notifer that read interface messages on a daemon
#returns Notifier
#
#
#close(self)
#closes and cleans the interface and its resources
#returns Nothing
#
#
#start(self)
#starts the interface and its resources
#returns Nothing
#
#read(self)
#reads from the and initializes a CanMessage
#returns CanMessage
#
#Write(self)
#Writes to the socket
#
#
#
#__iter__()
# reads from the socket and yields the can message
#

import socket
import struct
import threading
from gateway.can.message import CanMessage
from gateway.can.notifier import Notifier
DEFAULT_BUFFERSIZE = 16

class Interface:
    def __init__(self, address, listeners):
        self.listeners = listeners
        self.notifier = None
        self.address = address
        self.sock = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
        self.canDump = []

    def __str__(self):
        return str(self.sock.getsockname())

## may want to do more checking on system state before we close.
    def close(self):
        self.sock.close()

    def start(self):
        self.sock.bind((self.address,))
        self.launchNotifier()
        return True

    def read(self):
        recieved = self.sock.recv(DEFAULT_BUFFERSIZE)
        return CanMessage(recieved)

    def write(self,canmessage):
        #print('\nWriting: '+str(canmessage)+' bytes: '+str(canmessage.bytes())+'On Device:'+self.address)
        sent = self.sock.send(canmessage.bytes())
        return sent

    def launchNotifier(self):
        Notifier(self).launchDaemon()


#     def __iter__(self):
#         while True:
#             self.readSocket()
#         for message in self.canDump:
#             yield message
#         self.canDump = []

#     def _readToBufferLoop(self):
#         while True:
#             inmessage = self.readSocket()
#             self.canDump.append(inmessage)
#             #print('recieved and buffered message '+str(inmessage))

#     def readToBufferLoop(self):
#         threading.Thread(target=self._readToBufferLoop).start()
