from gateway.utils.gatewaycommand import GatewayCommand
from gateway.utils.creator import ProjectCreator
from gateway.can.configuration import Configuration, MisconfigurationExecption

class AppCommand(GatewayCommand):
    
    alias = 'a'
    description = "create a new application"

    def __init__(self,args):
        super().__init__(args)

    def run(self,arguments):
        options = {}
        project_create = ProjectCreator(arguments.name)
        project_create.build_project(**options)

    def extendArgparse(self,parser):
        parser.add_argument('name', help="The name of the Project")
