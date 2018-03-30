from gateway.utils.resourcelocator import ResourceLocator
from gateway.can.traffic.server import  Server, CoreHandler
from gateway.can.traffic.reciever import Receiver
from gateway.can.traffic.message import CanMessage
from gateway.can.control.errorhandler import ErrorHandler
from gateway.can.control.noticehandler import NoticeHandler
from gateway.can.control.notices import NewConnection
from gateway.core.server import Server as ServiceServer
from gateway.core.application import Application



import socket
import struct
import os
import sys
import logging
import threading
import queue
import json


"""
CAN Engine|
-----------

Daemon responsible for polling CAN Buses for incoming messages
and relaying to Core.

Nicholas and Federico
Amatruda and Rueda

"""

APP = "APPLICATION"
SERVER = "SERVER"
logger = logging.getLogger(__name__)

defautOptions = {'interfaces' : {}}

class Engine(object):
    conf = None
    can_outs = {}
    engine_server = None
    notices = queue.Queue()
    core_class = None

    receivers = []
    def __init__(self, *args, **options):
        options =  {**defautOptions, **options}
        super().__init__()

        self.load_engine(options['interfaces'])
        self.establish_core(Server,options)
        self.server_thread = threading.Thread(target=self.engine_server.serve_forever)
        self.start_recievers()

    def start_recievers(self):
        for receiver in self.receivers:
            receiver.start()

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

    def load_engine(self, interfaces):
        for address, interfaceType in interfaces.items():
                receiver = Receiver((address, interfaceType), self)
                self.receivers.append(receiver)
                self.can_outs[interfaceType] = receiver.socket_descriptor

        self.error_handler = ErrorHandler(self, **{'force_send' : True})
        self.notice_handler = NoticeHandler(self)

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
        current_thread = threading.current_thread()
        for thread in threading.enumerate():
            if thread is not current_thread and hasattr(thread,"service"):
                thread.clean_up()

                thread.join()

                thread.clean_up_r()

        sys.exit(1)

    """
    Daemon takes messages from the outgoing_buffer
    JSON string is converted to bytes and sent across CAN socket
    """

    def COREreceive(self,message):
        """
        Encoding functions go in here
        """
        return CanMessage.from_JSON(message)

    def COREsend(self,message):
        """
        Decoding functions go in here
        Subclass for more functionality
        """
        return message.to_JSON().encode()

    def Corenotice(self,message):
        pass


    def engine_notice(self,notice):
        self.queue_notice(notice)

    def engine_error(self,error):
        self.queue_notice(error)


    def queue_notice(self,notice):
        try:
            self.notices.put(notice)
        except queue.Full as msg:
            self.notifyEngine()

    def force_send(self,msg):
        pass

    def notifyEngine(self):
        pass

    @classmethod
    def getEngineType(cls,engine_type):
        """
        return an application engine or server engine
        """
        if engine_type == SERVER:
            return ServerEngine
        elif engine_type == APP:
            return ApplicationEngine
        else:
            return None

class ServerEngine(Engine):
    applications = []
    client_lock = threading.RLock()
    core_class = ServiceServer

    def __init__(self,*args, **options):
        super().__init__(*args,**options)
        self.max_connections = options['max_connections']
        self.core = ServiceServer(self)

    def COREreceive(self,message):
        message = super().COREreceive(message)
        self.core.handleMessage(message)

    def COREsend(self,message):
        enc_msg = super().COREsend(message)
        with self.client_lock:
            for application in self.applications:
                self.engine_server.socket.sendto(enc_msg, application)


    def COREnotice(self,message):
        pass

    def COREerror(self,message):
        pass



class ApplicationEngine(Engine):
    core_class = Application
    interface_types = []

    def __init__(self,*args, **options):
        super().__init__(*args,**options)
        self.core = Application(self)
        self.connect_to_server(options["server"])

    """
    For an Application that is not standalone interfaces are actually just expected types to be handled from
    the incoming core
    """
    def load_engine(self,interfaces):
        for address, interfaceType in interfaces.items():
            self.interface_types.append(interfaceType)

    def connect_to_server(self,server_address):
        self.COREnotice(NewConnection(self.engine_server.socket.getsockname()),server_address)

    def COREreceive(self,message):
        message = super().COREreceive(message)
        self.core.handleMessage(message)

    def COREsend(self,message):
        pass

    def COREnotice(self,message,server_address = None):
        if server_address is not None:
            self.engine_server.socket.sendto(message.TO_JSON().encode(),server_address)

    def COREerror(self,message):
        pass
