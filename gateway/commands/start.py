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

#Some examples of the adding arguments

        #optional argment
        #parser.add_argument('--foo', nargs='?', const='c', default='d', help="Woah")

        #positional arguements
        #parser.add_argument('bar', nargs='+', help='bar help')
