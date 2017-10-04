from gateway.utils.gatewaycommand import GatewayCommand
from gateway.utils import testfinder

class TestCommand(GatewayCommand):

    alias = 't'
    description = "begins the test routine"


    def __init__(self,args):
        super().__init__(args)

    def run(self,arguments):
        if(arguments.verbose):
            testfinder.run_tests(verbose=arguments.verbose)


    def extendArgparse(self,parser):
        parser.add_argument('--verbose', '-v', default="1",help='verbosity of tests',type=int)
        parser.add_argument('--modules','-m',default=None, help='specify modules to tests')
