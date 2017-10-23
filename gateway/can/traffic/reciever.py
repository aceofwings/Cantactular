"""
Responsible for litening and directing traffic to the engine.
Will forward data to a source using a callback function, provided by the engine.

Note: Reievers are not responsible for processing data.
"""

from threading import Thread
from socket import socket
class Reciever(Thread):

    def init(self):
        """
        Initialize a reciever with a function that will handle incoming data and
        a socket address
        :param forwards: A function that the reciever will forward its data too.
        """
        super().__init__(self,fowards,canSocket)
        self.daemon = True
        self.stopped = False
        self.forward = forwards
        self.canSocket = canSocket
        self.socket_address = socket_address

    def run(self):
        self.recieve_and_forward()

    def stop(self):
        self.stopped = True

    def recieve_and_forward(self):
        while not self.stopped:
            self.forward(self.canSocket.read())

class CanSocket(object)

    DEFAULT_BUFFERSIZE = 16

    def init(self):
        self.socket = socket(family=socket.AF_CAN)

    def __iter__(self):
        while True:
            yield self.socket.recv(self.DEFAULT_BUFFERSIZE)

    def read():
        return self.socket.recv(DEFAULT_BUFFERSIZE)

    def bind(self,address):
        self.socket.bind((address,))
