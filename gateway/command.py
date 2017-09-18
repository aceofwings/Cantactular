import argparse
import os
import pkgutil
from . import commands
from  importlib import import_module

#Package where commands are located
PACKAGE = "gateway.commands"

DESCRIPTION = "Collects and Recieves and Analyzes Data"

parser = argparse.ArgumentParser(description=DESCRIPTION)
listOfCommands = []
aliases = []

def loadCommandModules():
    modules = pkgutil.iter_modules([os.path.dirname(commands.__file__)])
    for module in modules:
        listOfCommands.append(module[1])

    executeCommand()

#loadCC - load Command content
def loadCC():
    pass

def executeCommand():
    args = parser.parse_args();
    print(args.command)

parser.add_argument("command")

loadCommandModules()
