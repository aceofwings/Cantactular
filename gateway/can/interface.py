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
    def __init__(self, address):
        self.listeners = []
        #controller Type
        self.ct = None
        self.active = False
        #notifier share amongst the program
        self.notifier = None
        self.address = address
        self.sock = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
        self.canDump = []

    def __str__(self):
        return str(self.sock.getsockname())

## may want to do more checking on system state before we close.
    def close(self):
        self.sock.close()


    def addListener(self,listener):
        self.listeners.append(listener)

    def start(self):
        self.sock.bind((self.address,))
        self.launchNotifier()

    def read(self):
        recieved = self.sock.recv(DEFAULT_BUFFERSIZE)
        self.active = True
        return CanMessage(recieved)

    def write(self,canmessage):
        #print('\nWriting: '+str(canmessage)+' bytes: '+str(canmessage.bytes())+'On Device:'+self.address)
        if self.active:
            sent = self.sock.send(canmessage.bytes())
            return sent
        else:
            raise InterfaceError()
            return 0

    def launchNotifier(self):
        Notifier(self).launchDaemon()

class InterfaceError(Exception):
    __init__(self):
        print('Interface not active!')
