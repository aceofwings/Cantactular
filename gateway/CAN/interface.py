#Authors: Nicholas Amatruda
#
#
#Interface defines a virtual representation of the physical CAN interface
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
from gateway.CAN.message import CanMessage
from gateway.CAN.notifier import Notifier
DEFAULT_BUFFERSIZE = 16

class Interface:
    def __init__(self, address):
        self.notifier = None
        self.address = address
        self.sock = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)

    def __str__(self):
        return str(self.sock.getsockname())
## may want to do more checking on system state before we close.
    def close(self):
        self.sock.close()

    def start(self):
        try:
            self.sock.bind((self.address,))
        except socket.error as e:
            print("Socket error binding: "+e.mesg)
            return False
        return True

    def read(self):
        recieved = self.sock.recv(DEFAULT_BUFFERSIZE)
        return CanMessage(recieved)

    def write(self,canmessage):
        sent = self.sock.send(canmessage.bytes())
        return sent

    def launchNotifier(self):
        return Notifier()

    def __iter__(self):
        yield self.read()

