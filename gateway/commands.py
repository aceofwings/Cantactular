import argparse
import os
# Parse our arguments
from gateway.CAN.controller import Controller
from gateway.CAN.message import CanMessage
from gateway.utils.projectpaths import ProjectPath
from gateway.CAN.listener import Listener

def test():
    import tests.runtest

def start():
    print("starting")

    kicktheCAN = Controller()

    earsThatHear = Listener()
    kicktheCAN.addListener(earsThatHear)

    can0 = kicktheCAN.addInterface("vcan0")[0]
    kicktheCAN.startInterface()

    #objdic = ObjectDictionary.initialize(ProjectPath.edsfile('MotorController.eds'))

    canmessage = CanMessage.create(1694, b'Tis8Byts')

    sent = can0.write(canmessage)
    sent = can0.write(canmessage)
    sent = can0.write(canmessage)

    while True:
        for mesg in can0:
            print("Captured by the muthafucking listener bitch")

commands = ['start','test','logger']

startFunctions = {'start' : start, 'test' : test}

parser = argparse.ArgumentParser(description = "Arugment Handling for bin/gateway")

parser.add_argument('process', help='Run the main application', choices=commands)
args = parser.parse_args()

##
startFunctions[args.process]()
