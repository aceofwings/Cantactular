#Authors: (Please put name here)
#
#
#Interface defines a virtual representation of the physical CAN interface
#These interfaces usually are defined by a CANIP or NIC name, eg CAN0
#
#
#
#

class Interface:
        def __init__(self):
            self.notifier = None
        def initialize(self):
            pass
        def close(self):
            pass
        def read(self):
            return CanMessage()
        def write(self,canmessage):
            return bytes()
        def launchNotifier(self):
            return Notifier()
