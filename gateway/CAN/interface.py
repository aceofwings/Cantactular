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

import Socket
class Interface:
        def __init__(self, controller, device):
            self.notifier = None
		    self.controller = controller
		    self.device = device
            self.sock = None

        def close(self):
            pass

        def start(self):
            pass

        def read(self):
            return CanMessage()

        def write(self,canmessage):
            return bytes()

        def launchNotifier(self):
            return Notifier()

        def __iter__():
            yield self.read()
