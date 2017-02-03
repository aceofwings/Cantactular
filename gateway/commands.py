import argparse
# Parse our arguments


def test():
    import tests.runtest

def start():
    print("starting")

commands = ['start','test','logger']

startFunctions = {'start' : start, 'test' : test}

parser = argparse.ArgumentParser(description = "Arugment Handling for bin/gateway")

parser.add_argument('process', help='Run the main application', choices=commands)
args = parser.parse_args()

##
startFunctions[args.process]()
