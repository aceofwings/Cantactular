#
#
#
#Notifer will be initialize with an interface and will
#
#
#
#
#
#
#
#
class Notifier:
    def __init__(self,interface):
        self.interface = interface
        self.listeners = []
        self.thread = None
    #Listen on interface and notify all listeners
    #
    # Returns None
    def notifyAll(self,canmessage):
        pass
