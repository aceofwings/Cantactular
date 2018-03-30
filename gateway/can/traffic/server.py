import socketserver as SocketServer
from gateway.utils.resourcelocator import ResourceLocator


class Server(SocketServer.UnixDatagramServer):

    engine = None

class CoreHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request[0]
        address = self.request[1]
        self.server.engine.COREreceive(data.decode())

    def server_close(self):
        pass
