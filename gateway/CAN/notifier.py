#
#
#
#Notifer will be initialize with an interface and will launch its own daemon.
#
#
#
#
#
from threading import Thread

class Notifier:
    def __init__(self,interface):
        self.thread = None

    def launchDaemon():
        pass

    def stopDaemon():
        pass
    #Listen on interface and notify all listeners
    #
    # Returns None
    def readloop(self, listeners):
        pass
