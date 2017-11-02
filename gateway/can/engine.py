from gateway.can.traffic.reciever import Receiver
from gateway.utils.resourcelocator import ResourceLocator

import socket
import struct
import json
import os
import logging
import enum
import threading
"""
CAN Engine|
-----------

Daemon responsible for polling CAN Buses for incoming messages
and relaying to Core.

Nicholas and Federico
Amatruda and Rueda

"""

logger = logging.getLogger(__name__)

class Engine(object):

    class EngineNotices(enum.Enum):
        NEW_CONNECTION = "A new connection was made"

    class EngineErrors(enum.Enum):
        TOO_MANY_CONNECTIONS = "To many connections to engine"

    receivers = []
    outlets = []
    clients = []

    core_socket =  socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    conf = None

    def __init__(self, *args, **options):
        super().__init__()
        def load_engine():
            for address, interfaceType in options['interfaces'].items():
                    receiver = Receiver((address, interfaceType), self)
                    self.receivers.append(receiver)

        def establish_core():
            tempfolder = ResourceLocator.get_locator(relative_path="temp")
            if options['core_address'] in options:
                full_path = tempfolder.fetch_file_path('core.out')
            else:
                full_path = tempfolder.fetch_file_path(options['core_address'])
            try:
                os.unlink(full_path)
            except OSError:
                if os.path.exists(full_path):
                    print("The path exists")
            try:
                self.core_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
                self.core_socket.bind(full_path)
                self.core_socket.listen(1)
            except socket.error as msg:
                self.core_socket.close()
                self.core_socket = None
            except OSError as msg:
                print(msg)

        def start_recievers():
            for receiver in self.receivers:
                receiver.start()
        #
        load_engine()
        establish_core()
        start_recievers()
        #
        #
        #
        while True:
            pass
    def start(self):
        pass

    def accept_clients(self):
        while True:
            connection,client_address = self.core_socket.accept()
            if self.clients.length() < self.conf.maximum_number_connections():
                self.clients.append(connection)
                self.COREsend({'notice': EngineNotices.NEW_CONNECTION})
            else:
                self.COREerror({'error': EngineErrors.TOO_MANY_CONNECTIONS, 'msg': "Cannot open request"  }, connection)
                connection.close()
                self.notifyEngine(notice=EngineNotices.NEW_CONNECTION)

    def avaiable_outlets(self):
        return {"CANOPEN" : CanOpenOutlet, "EVTCAN" : EvtCanOutlet, "DEFAULT" : CanOutlet}
    """
    Takes Can Packet as list of 16 bytes, the network, type and endian of data
    bytes: list of integers, length should be 16
    CAN Frame: CANID (4) , DataLen (1) , Padding (3) , Data (0 - 8)(Big Endian)
    Returns JSON string
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
    def from_JSON(self,json,endian):
        messagedata = json.loads(json)
        fstring = b'<IB3x8s' if endian == 'little' else b'>IB3x8s'
        can = struct.pack(fstring, messagedata['canid'], messagedata['datalen'], bytes(messagedata['data']))
        can = list(can)
        can[8:] = (bytes(messagedata['data']))
        for i in range(8, 16 - messagedata['datalen']):
            can.insert(i, 0)
        can = bytes(can)
        return can, messagedata['network'], messagedata['type']


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
    def CANsend(self):
        pass



    def COREsend(self,message,socket=None):
        """
        Daemon unpacks Canmessage and structures it as a dictionary, ultimately
        passed to COREsend.

        The message format depends on the type of outlet the engine uses.
        There are two types of outlets one instiated for each interface.

        They decorate a message with type of frame.

        """
        print(message)
        for client in self.clients:
            client.sendall(self.to_JSON(message).encode())


    def COREerror(self,message,socket=None):
        """
        Recieve messages and foward them as errors to core applications. Will determine
        wether the error is recoverable
        """
        print(message)

    def COREreceive(self):
        """
        Daemon polls the core socket for messages in JSON
        Places core messages in outgoing_buffer if message type is CAN
        Handles other events as necessary
        """
        pass

    def notifyEngine(notice=None):
        pass
