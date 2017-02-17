import os
from gateway.utils.projectpaths import common
#
#
#
#
#Test Finder will find and search for test given the specifications
#
#
#

def loadTestFiles():
    modules = []
    for directory in os.listdir(common.tests):
        directoryPath = os.path.join(common.tests,directory)
        if os.path.isdir(directoryPath):
            directoryCheck = os.listdir(directoryPath)
            for testMod in directoryCheck:
                if testMod == '__init__.py':
                    modules.append(directoryPath)
    return modules

def executeTests():
    pass
