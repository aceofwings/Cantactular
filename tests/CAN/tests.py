import unittest
from gateway.utils.testfinder import loadTestModulesfromArray

#NOTE by providing a load_tests() function will be called to help load anything
#from the subdirectories.
#


submoduleTests = [
'tests.can.message.test',
'tests.can.controller.test',
'tests.can.interface.test',
'tests.can.notifier.test',
'tests.can.listener.test'
]





#
#Load test from subpackages
#
def load_tests(loader, tests, pattern):
    return  loadTestModulesfromArray(submoduleTests)
