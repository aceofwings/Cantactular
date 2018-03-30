from gateway.utils.gatewaycommand import GatewayCommand
from gateway.utils import testfinder

class TestCommand(GatewayCommand):

    alias = 't'
    description = "begins the test routine"


    def __init__(self,args):
        super().__init__(args)

    def run(self,arguments):

        super().run(arguments)

        if(arguments.verbose):
            testfinder.verbosity = arguments.verbose

        if not testfinder.run_tests(arguments.classes):
            print("Could not find test cases")



    def extendArgparse(self,parser):
        parser.add_argument('--verbose', '-v', default="1",help='verbosity of tests',type=int)
        parser.add_argument('--classes','-c',default=None, nargs='*', help='specify class to test')
