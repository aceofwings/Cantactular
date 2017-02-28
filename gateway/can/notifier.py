#
#
#
#Notifer will be initialize with an interface and will launch its own daemon.
#
#
#
#
#
import threading

class Notifier:
    def __init__(self,interface):
        self.thread = None
        self.interface = interface
        self.daemonThread = threading.Thread(target=self.readloop)
        self.daemonThread.setDaemon(True)
        self._stop = threading.Event()

    def launchDaemon(self):
        if not self.daemonThread.isAlive():
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
            message = self.interface.read()
            for listener in self.interface.listeners:
                listener.notify(mesg)
            if self._stop.isSet():
                return 0

#             for mesg in self.interface:
#                 for listener in self.interface.listeners:
#                     listener.notify(mesg)
#
