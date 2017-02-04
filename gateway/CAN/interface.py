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

import Socket
import threading.Thread

class Interface:
        def __init__(self, controller, device):
        	self.notifier = None
		self.controller = controller
		self.device = device

        def close(self):
            pass

        def read(self):
            return CanMessage()

        def write(self,canmessage):
            return bytes()

        def launchNotifier(self):
            return Notifier()
