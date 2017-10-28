from gateway.can.forwarders.canopenout import CanOpenOutlet
from gateway.can.forwarders.evtout import EvtCanOutlet
from gateway.can.forwarders.canout import CanOutlet
from gateway.can.configuration import Configuration
from gateway.can.traffic.reciever import Receiver
from gateway.utils.resourcelocator import ResourceLocator
import socket
import time
import struct
import json

"""
CAN Engine|
-----------

Daemon responsible for polling CAN Buses for incoming messages
and relaying to Core.

Nicholas and Federico
Amatruda and Rueda

"""


class Engine(object):

    receivers = []
    outlets = []

    core_socket =  socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    conf = None

    def __init__(self):
        super().__init__()

        def load_engine():
            self.conf = Configuration()
            conf_interfaces = self.conf.interfaces()
            if conf_interfaces is None:
                raise EnvironmentError
            for address, interfaceType in conf_interfaces.items():
                if interfaceType in self.avaiable_outlets():
                    outlet = self.avaiable_outlets()[interfaceType](self)
                    self.outlets.append(outlet)
                    reciever = Receiver(address, outlet)
                    self.receivers.append(reciever)
                else:
                    outlet = self.avaiable_outlets()["DEFAULT"](self, message_type=interfaceType)
                    self.outlets.append(outlet)
                    reciever = Receiver(address, outlet)


        def establish_core():
            if self.conf is None:
                self.conf = Configuration()
            tempfolder = ResourceLocator.get_locator(relative_path="temp")
            if self.conf.core_socket_address() is None:
                pass
            full_path = tempfolder.fetch_file_path(self.conf.core_socket_address())

            try:
                self.core_socket.bind(full_path)
            except socket.error as msg:
                self.core_socket.close()
                self.core_socket = None

        def start_recievers():
            for receiver in self.receivers:
                receiver.start()

        load_engine()
        establish_core()
        start_recievers()

        while True:
            pass

    def avaiable_outlets(self):
        return {"CANOPEN" : CanOpenOutlet, "EVTCAN" : EvtCanOutlet, "DEFAULT" : CanOutlet}
    """
    Takes Can Packet as list of 16 bytes, the network, type and endian of data
    bytes: list of integers, length should be 16
    CAN Frame: CANID (4) , DataLen (1) , Padding (3) , Data (0 - 8)(Big Endian)
    Returns JSON string
    """
    def to_JSON(self,bytes,network,type,endian):
        messagedata = {'time': time.time()}
        messagedata['canid'] = -1
        messagedata['datalen'] = -1
        messagedata['data'] = -1
        messagedata['network'] = None
        messagedata['type'] = None
        if bytes is not None:
            messagedata['canid'] = int.from_bytes(bytes[0:4], byteorder=endian)
            messagedata['datalen'] = int(bytes[4])
            if messagedata['datalen'] == 0:
                messagedata['data'] = [0]
            else:
                messagedata['data'] = list(bytes[(16 - messagedata['datalen']):])
            messagedata['network'] = network
            messagedata['type'] = type
        return json.dumps(messagedata)

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



    def COREsend(self,message):
        """
        Daemon sends messages from incoming_buffer to core
        """
        print(message)

    def COREerror(self,message):
        """
        Daemon sends error messages from incoming_buffer to core
        """
        print(message)

    def COREreceive(self):
        """
        Daemon polls the core socket for messages in JSON
        Places core messages in outgoing_buffer if message type is CAN
        Handles other events as necessary
        """
        pass
