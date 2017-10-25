"""
Responsible for litening and directing traffic to the engine.
Will forward data to a source using a callback function, provided by the engine.

Note: Reievers are not responsible for processing data.
"""

import threading
import socket

class Receiver(object):

    def __init__(self,address,outlet):
        """
        Initialize a reciever with a function that will handle incoming data and
        a socket address
        :param forwards: A function that the reciever will forward its data too.
        """
        super().__init__()
        self.stopped = False
        self.outlet = outlet
        self.canSocket = CanSocket(address)
        self.daemonThread = threading.Thread(target=self.recieve_and_forward)
        self.daemonThread.setDaemon(True)
        self._stop = threading.Event()

    def start(self):
        if not self.daemonThread.isAlive():
            try:
                self.canSocket.bind()
            except socket.error as msg:
                self.outlet.forward_error(socket.error,msg)
                
                return 0
            self.daemonThread.start()

    def stop(self):
        self._stop.set()

    def recieve_and_forward(self):
        self.canSocket.socket.settimeout(5)

        try:
            while not self._stop.isSet():
                self.forward(self.canSocket.read())
        except socket.timeout, msg:
            self.outlet.forward_error(socket.timeout, msg)

    def attempt_recovery():
        pass

class CanSocket(object):

    DEFAULT_BUFFERSIZE = 16
    address = None

    def __init__(self,address):
        self.socket = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
        self.address = address

    def __iter__(self):
        while True:
            yield self.socket.recv(self.DEFAULT_BUFFERSIZE)

    def read(self):
        return self.socket.recv(self.DEFAULT_BUFFERSIZE)

    def bind(self):
        self.socket.bind((self.address,))
