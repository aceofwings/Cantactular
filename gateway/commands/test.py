from gateway.utils.gatewaycommand import GatewayCommand

class StartCommand(GatewayCommand):

    alias = 's'

    def __init__(self,arguments):
        super().__init__(self,arguments)

    def run(self):
        print("starting gateway")
