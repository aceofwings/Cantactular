from gateway.utils.gatewaycommand import GatewayCommand
from gateway.can.configuration import Configuration, MisconfigurationExecption
from gateway.can.engine import Engine
import sys

class StartCommand(GatewayCommand):

    alias = 's'
    description = "starts logging data"

    def __init__(self,args):
        super().__init__(args)

    def run(self,arguments):

        options = {}
        try:
            self.conf = Configuration(environment=arguments.environment)
        except MisconfigurationExecption as msg:
            print(msg)
            sys.exit(1)
        if self.conf.interfaces() is not None:
            options['interfaces'] = self.conf.interfaces()
        else:
            raise MisconfigurationExecption("There are no interfaces configured")
            sys.exit(1)

        if self.conf.core_socket_address is not None:
            options["core_address"] = self.conf.core_socket_address()
        else:
            raise MisconfigurationExecption("No core socket address")
        try:
            Engine(**options).start()
        except KeyboardInterrupt as msg:
            print("Exiting...")
            sys.exit(0)


    def extendArgparse(self,parser):
        parser.add_argument('--environment','--e', default='development', help="Choose the environment")
