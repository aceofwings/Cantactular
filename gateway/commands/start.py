from gateway.utils.gatewaycommand import GatewayCommand
from gateway.can.configuration import Configuration, MisconfigurationExecption
from gateway.can.engine import Engine,APP,SERVER
import sys

class StartCommand(GatewayCommand):

    alias = 's'
    description = "starts logging data"

    def __init__(self,args):
        super().__init__(args)

    def run(self,arguments):
        options = {}
        super().run(arguments)
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

        if arguments.location is not None:
            options["core_address"] = arguments.location
        elif self.conf.core_socket_address is not None:
            options["core_address"] = self.conf.core_socket_address()
        else:
            raise MisconfigurationExecption("No core socket address")
        if self.conf.core_type is None:
            raise MisconfigurationExecption("No core type specificed")

        options["service"] = self.conf.core_type()
        options["server"]  = self.conf.server_address()

        if self.conf.limit_connection():
            options["max_connections"] = self.conf.max_ipc_connections()
        else:
            options["max_connections"] = None


        if self.conf.core_type() == APP and arguments.server is not None:
            options["server"] = arguments.server

        engine  = Engine.getEngineType(self.conf.core_type())(**options)


        try:
            engine.start()
        except KeyboardInterrupt as msg:
            print("Exiting...")
            engine.shutdown()
            sys.exit(0)
        except SystemExit as msg:
            print("Exiting Application")


    def extendArgparse(self,parser):
        parser.add_argument('--location', help="Absolute path of the IPC socket")
        parser.add_argument('--server','--s', help="specify server location")
        parser.add_argument('--environment','--e', default='development', help="Choose the environment")
