from gateway.utils.gatewaycommand import GatewayCommand

class StartCommand(GatewayCommand):

    alias = 's'
    description = "starts logging data"

    def __init__(self,args):
        super().__init__(args)

    def run(self,arguments):
        print("starting gateway")
        
    def extendArgparse(self,parser):
        pass
