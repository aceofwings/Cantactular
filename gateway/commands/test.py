from gateway.utils.gatewaycommand import GatewayCommand

class TestCommand(GatewayCommand):

    alias = 't'
    description = "begins the test routine"


    def __init__(self,args):
        super().__init__(arguments)

    def run(self,arguments):
        print("starting gateway")
