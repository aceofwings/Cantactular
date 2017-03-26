import argparse
import os
from  gateway.apps.terminal import Terminal

# Parse our arguments

def test():
    import tests.runtest

def start():
    Terminal().start()


commands = ['start','test','logger']

startFunctions = {'start' : start, 'test' : test}

parser = argparse.ArgumentParser(description = "Arugment Handling for bin/gateway")

parser.add_argument('process', help='Run the main application', choices=commands)
args = parser.parse_args()

##
startFunctions[args.process]()
