import argparse
import os
import pkgutil
import inspect
from . import commands
from  importlib import import_module

#Package where commands are located
PACKAGE = "gateway.commands"

DESCRIPTION = "Collects and Recieves and Analyzes Data"

parser = argparse.ArgumentParser(description=DESCRIPTION, add_help=False)

parser.add_argument('--commands', action='help', default=argparse.SUPPRESS,
                    help='list the commands available')
listOfCommands = {}


def loadCommandModules():
    modules = pkgutil.iter_modules([os.path.dirname(commands.__file__)])
    for module in modules:
        listOfCommands[module[1]] = import_module('.' + module[1], PACKAGE)

    parser.add_argument('service', choices=listOfCommands.keys())

    try:
        executeCommand()
    except ClassNonExistent as e:
        print(str(e) + " " + e.errors)

#TODO load command content such as aliases for commands and aliases assigned
#to bundle commands
def loadCC():
    pass

def executeCommand():
    arg, options = parser.parse_known_args()
    if arg.service not in listOfCommands:
        parser.print_help()
        parser.exit()

    commandModule = listOfCommands[arg.service]
    members = inspect.getmembers(commandModule, inspect.isclass)
    commandclass = list(filter(lambda name: name[0].upper() == arg.service.upper() + "COMMAND" , members))

    if not commandclass:
        raise ClassNonExistent("Could not find the command class", arg.service.capitalize() + "Command")

    commandClass = getattr(commandModule, commandclass[0][0])
    commandClass(options).execute()

class ClassNonExistent(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors



loadCommandModules()
