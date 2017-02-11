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
    def __init__(self,interface, listeners):
        self.thread = None
        self.listeners = listeners
        self.interface = interface
        self.daemonThread = Thread.thread(target=readloop)
        self.daemonThread.setDaemon(True)
        self._stop = threading.Event()

    def launchDaemon(self):
        if self.daemonThread.isAlive():
            self.daemonThread.start()
        else:
            raise threading.ThreadError("Daemon is alive anad running")

    def stopDaemon():
        self._stop.set()
    #Listen on interface and notify all listeners
    #
    # Returns None
    def readloop(self):
        while True:
            for mesg in self.interface:
                for listener in self.listeners:
                    listener.notify(mesg)
                if self._stop.isSet():
                    return 0
