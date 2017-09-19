from gateway.utils.gatewaycommand import GatewayCommand

class StartCommand(GatewayCommand):

    alias = 's'

    def __init__(self):
        super().__init__(self)

    def run(self):
        print("starting gateway")
