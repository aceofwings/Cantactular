from gateway.utils.gatewaycommand import GatewayCommand
from gateway.commands import start
import os

class ServerCommand(GatewayCommand):
    description = "Start a basic Server for applications to listen on"

    INSTALL_PATH = '/etc/gateway'

    def __init__(self,args):
        super().__init__(args)
        self.startCommand = start.StartCommand(args)


    def run(self, arguments):
        os.chdir(self.INSTALL_PATH)
        self.startCommand.run(arguments)

        options = {}


    def extendArgparse(self,parser):
        self.startCommand.extendArgparse(parser)
