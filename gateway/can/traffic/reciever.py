"""
Responsible for litening and directing traffic to the engine.
Will forward data to a source using a callback function, provided by the engine.

Note: Reievers are not responsible for processing data.
"""

import threading
import socket
import ctypes
import fcntl
import array
import struct
import time

from gateway.can.control.errors import CanSocketTimeout
from gateway.can.control.errorhandler import BaseErrorTypes
from gateway.can.traffic.canout import CanOutlet


SIOCGSTAMP = 0x8906
SO_TIMESTAMPNS = 35

class TIME_VALUE(ctypes.Structure):
    _fields_ = [("tv_sec", ctypes.c_ulong),
    ("tv_usec", ctypes.c_ulong)]

class Receiver(object):

    def __init__(self,socketInfo,engine):
        """
        Initialize a reciever with a function that will handle incoming data and
        a socket address
        :param forwards: A function that the reciever will forward its data too.
        """
        super().__init__()
        address, type = socketInfo
        self.stopped = False
        self.outlet = CanOutlet(engine, message_type=type)
        self.canSocket = CanSocket(address)
        self.daemonThread = threading.Thread(target=self.recieve_and_forward)
        self.daemonThread.setDaemon(True)
        self._stop = threading.Event()
        self.time_buffer = array.array('B', [0] * 8)

        #Setting the SO_TIMESTAMPNS option will allow the frame to  be recieved with additional ancillary data.
        #The time stamp is now generated  when the interupt is recieved to read from the socket.``
        self.canSocket.socket.setsockopt(socket.SOL_SOCKET, SO_TIMESTAMPNS,1)

    def start(self):
        if not self.daemonThread.isAlive():
            try:
                self.canSocket.bind()
            except socket.error as msg:
                self.outlet.forward_error(msg)
                return 0

            self.daemonThread.start()

    def stop(self):
        self._stop.set()

    def recieve_and_forward(self):
        self.canSocket.socket.settimeout(5)
        try:
            while not self._stop.isSet():
                self.outlet.forward(self.canSocket.read())
        except socket.timeout as msg:
            error = BaseErrorTypes.SOCKET_TIMEOUT()
            error.socket = self.socket_descriptor()
            self.outlet.forward_error(error)
            self._stop.set()

    def attempt_recovery(self):
        pass

    @property
    def socket_descriptor(self):
        return self.canSocket.socket

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
        #return self.socket.recv(self.DEFAULT_BUFFERSIZE)
        msg = self.socket.recvmsg(self.DEFAULT_BUFFERSIZE,32)
        return (msg[0], msg[1][0][2])

    def bind(self):
        self.socket.bind((self.address,))
