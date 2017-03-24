import argparse
import os
# Parse our arguments
from gateway.utils.projectpaths import ProjectPath
from gateway.can.controller import Controller
from gateway.can.message import CanMessage
from gateway.can.listener import Listener

def test():
    import tests.runtest

def start():
    print("starting CAN controller on vcan0")


commands = ['start','test','logger']

startFunctions = {'start' : start, 'test' : test}

parser = argparse.ArgumentParser(description = "Arugment Handling for bin/gateway")

parser.add_argument('process', help='Run the main application', choices=commands)
args = parser.parse_args()

##
startFunctions[args.process]()
