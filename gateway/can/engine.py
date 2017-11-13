from gateway.utils.resourcelocator import ResourceLocator
from gateway.can.traffic.server import  Server, CoreHandler
from gateway.can.traffic.reciever import Receiver
from gateway.can.control.errorhandler import ErrorHandler
from gateway.can.control.noticehandler import NoticeHandler
from gateway.can.control.notices import Notice
from gateway.can.controllers import base, error,internal

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
    applications = []
    conf = None
    can_outs = {}
    controllers = {}
    client_lock = threading.RLock()
    engine_server = None
    notices = queue.Queue()

    receivers = []
    def __init__(self, *args, **options):
        options =  {**defautOptions, **options}
        super().__init__()
        def load_engine():
            for address, interfaceType in options['interfaces'].items():
                    receiver = Receiver((address, interfaceType), self)
                    self.receivers.append(receiver)
                    self.can_outs[interfaceType] = receiver.socket_descriptor

            self.error_handler = ErrorHandler(self, **{'force_send' : True})
            self.notice_handler = NoticeHandler(self)
            self.controllers = self.get_controllers()

        def start_recievers():
            for receiver in self.receivers:
                receiver.start()

        load_engine()
        self.establish_core(Server,options)
        start_recievers()
        self.server_thread = threading.Thread(target=self.engine_server.serve_forever)

    def establish_core(self,server_cls,options):
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
            self.engine_server = server_cls(full_path, CoreHandler)
            self.engine_server.engine = self
        except socket.error as msg:
            pass
        except OSError as msg:
            print(msg)

    def start(self):
        self.server_thread.start()
        while True:
            try:
                engine_msg = self.notices.get()

                if issubclass(type(engine_msg), Exception):
                    self.error_handler.handle_error(engine_msg)
                else:
                    self.notice_handler.handle_notice(engine_msg)
            except queue.Empty as msg:
                print(msg)

    def shutdown(self):
        self.engine_server.shutdown()
        #handle errors in queue if there are any and send out any messages

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
    Daemon takes messages from the outgoing_buffer
    JSON string is converted to bytes and sent across CAN socket
    """
    def CANsend(self,message):
        self.can_outs[message['type']].send(bytes([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))

    def COREsend(self,message,socket=None):
        """
        Daemon unpacks Canmessage and structures it as a dictionary, ultimately
        passed to COREsend.

        The message format depends on the type of outlet the engine uses.
        There are two types of outlets one instiated for each interface.

        They decorate a message with type of frame.

        """
        with self.client_lock:
            data = self.to_JSON(message).encode()
            for application in self.applications:
                self.engine_server.socket.sendto(data, application)

    def get_controllers(self):
        return {"EVTCAN" : base.EvtCanController(self), "OPENCAN": base.OpenCanController(self),
        "ENGINE": internal.InternalController(self), "ERROR" : error.ErrorController(self),
        "MISC": base.MiscController(self)}

    def COREerror(self,message):
        """
        Recieve messages and foward them as errors to core applications. Will determine
        wether the error is recoverable
        """

    def engine_notice(self,notice):
        self.queue_notice(notice)

    def engine_error(self,error):
        self.queue_notice(error)


    def COREreceive(self,message):
        """
        Server forwards incoming message from engine
        """
        can_d = json.loads(message.decode())
        self.controllers[can_d['type']].handle_message(can_d)
        return can_d

    def queue_notice(self,notice):
        try:
            self.notices.put(notice)
        except queue.Full as msg:
            self.notifyEngine()

    def force_send(self,msg):
        pass

    def notifyEngine(self):
        pass
