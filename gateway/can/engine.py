from gateway.utils.resourcelocator import ResourceLocator
from gateway.can.traffic.server import  Server, CoreHandler
from gateway.can.traffic.reciever import Receiver
from gateway.can.control.handler import BasicMessageHandler
from gateway.can.control.errorhandler import ErrorHandler

import socket
import struct
import json
import os
import logging
import threading
import queue

"""
CAN Engine|
-----------

Daemon responsible for polling CAN Buses for incoming messages
and relaying to Core.

Nicholas and Federico
Amatruda and Rueda

"""

logger = logging.getLogger(__name__)

defautOptions = {'interfaces' : {}}

class Engine(object):

    engine_server = None
    engine_handler = None
    conf = None
    errors = queue.Queue()
    receivers = []
    def __init__(self, *args, **options):
        options =  {**defautOptions, **options}
        super().__init__()
        def load_engine():
            for address, interfaceType in options['interfaces'].items():
                    receiver = Receiver((address, interfaceType), self)
                    self.receivers.append(receiver)

            self.engine_handler = BasicMessageHandler(self)
            self.error_handler = ErrorHandler(self, {force_send : True})

        def establish_core():
            tempfolder = ResourceLocator.get_locator(relative_path="temp")
            if 'core_address' not in options:
                full_path = tempfolder.fetch_file_path('core.out')
            else:
                full_path = tempfolder.fetch_file_path(options['core_address'])
            try:
                 os.unlink(full_path)
            except OSError:
                if os.path.exists(full_path):
                    print("The path exists")
            try:
                self.engine_server = Server(full_path, CoreHandler)
            except socket.error as msg:
                pass
            except OSError as msg:
                print(msg)

        def start_recievers():
            for receiver in self.receivers:
                receiver.start()

        load_engine()
        establish_core()
        start_recievers()

        while True:


    def start(self):
        self.engine_server.serve_forever()


    """
    Takes Can Packet as list of 16 bytes, the network, type and endian of data
    bytes: list of integers, length should be 16
    CAN Frame: CANID (4) , DataLen (1) , Padding (3) , Data (0 - 8)(Big Endian)
    Returns JSON string that can be encoded
    """
    def to_JSON(self,message):
        dlc =  message['message']['dlc']
        if dlc == 0:
            message['message']['data'] = [0]
        else:
            message['message']['data'] = list(message['message']['data'][0: 16 - dlc])
        return json.dumps(message)

    """
    Takes the formatted JSON string and convert it to CAN Frame (list of 16 bytes)
    and endian of data.
    Returns a tuple of bytes list,network,type
    """
    def from_JSON(self,line):
        message = json.loads(line)
        messagedata = message['message']
        fstring = b'<IB3x8s'

        can = struct.pack(fstring, messagedata['canid'], messagedata['dlc'], bytes(messagedata['data']))
        can = list(can)

        can[8:] = (bytes(messagedata['data']))
        for i in range(8, 16 - messagedata['dlc']):
            can.insert(i, 0)
        can = bytes(can)
        return can, message['type']


    """
    Creates and binds the sockets of the CAN engine to the default_addresses list.
    Returns with GLOBAL list of socket objects instantiated
    """
    def bindsockets(self):
        pass

    """
    Daemon reads the CAN Bus specified by socket connection input
    Messages recieved are converted to JSON and placed into incoming_buffer
    """
    def CANread(self):
        pass

    """
    Daemon takes messages from the outgoing_buffer
    JSON string is converted to bytes and sent across CAN socket
    """
    def CANsend(self,message):
        message = self.from_JSON(message)




    def COREsend(self,message,socket=None):
        """
        Daemon unpacks Canmessage and structures it as a dictionary, ultimately
        passed to COREsend.

        The message format depends on the type of outlet the engine uses.
        There are two types of outlets one instiated for each interface.

        They decorate a message with type of frame.

        """
        self.to_JSON(message).encode()


    def COREerror(self,message):
        """
        Recieve messages and foward them as errors to core applications. Will determine
        wether the error is recoverable
        """

    def engine_error(self,message):
        self.queue_error(message)


    def COREreceive(self,message):
        """
        Daemon polls the core socket for messages in JSON
        Places core messages in outgoing_buffer if message type is CAN
        Handles other events as necessary
        """
        can_d = json.loads(message.decode())

        self.engine_handler.setup_and_handle(can_d['type'], can_d['message'])

        return can_d

    def queue_error(self,error):
        try:
            self.errors.put(error)
        except queue.Full as msg:
            self.notifyEngine()

    def force_send(self,msg):
        pass

    def notifyEngine(notice=None):
