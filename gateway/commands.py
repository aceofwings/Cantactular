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

    controller = Controller()
    controller.createInterface("vcan0")
    testmessage = CanMessage().create(0x762,'DEADBEEF')
    check = controller.write(testmessage)
    print("sent this many bytes: "+str(check)+"\nwaiting for responses to listener")
    listener = Listener()
    controller.addListener(listener)

    while True:
        pass


commands = ['start','test','logger']

startFunctions = {'start' : start, 'test' : test}

parser = argparse.ArgumentParser(description = "Arugment Handling for bin/gateway")

parser.add_argument('process', help='Run the main application', choices=commands)
args = parser.parse_args()

##
startFunctions[args.process]()
