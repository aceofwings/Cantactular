import os
from  importlib import import_module
#import_module(name, package=None)
#
from gateway.utils.projectpaths import common
import unittest
#
#
#Test Finder will find and search for test given the specifications
#Each main module ( CAN, Utils) will have its own tests.py
#
#tests.py must contain classes that inherit from unittest and the appropriate
#prefixes for functions. Eg. test_name
#
#Each test must also assert something or skip. It cannot do both.
#
TEST_PATH = common.tests
TEST_MODULE = '.tests'
#
#Use a default loader provied by unittest.
#
testLoader = unittest.defaultTestLoader
#
#Use default test Runner four  our test cases
#
testRunner = unittest.TextTestRunner(verbosity=2)
#find  modules
def findTestModules():
    modules = []
    for directory in os.listdir(common.tests):
        directoryPath = os.path.join(common.tests,directory)
        if os.path.isdir(directoryPath):
            directoryCheck = os.listdir(directoryPath)
            for testMod in directoryCheck:
                if testMod == '__init__.py':
                    modules.append(os.path.basename(directoryPath))
    return modules
#load  modules
def loadTestModules():
    testing = []
    testmodules = findTestModules()
    for module in testmodules:
         testing.append(import_module('tests.' + module + TEST_MODULE))
    return testing

#begin testing
def startTestSequence():
    modules = loadTestModules()
    for module in modules:
        test = testLoader.loadTestsFromModule(module)
        testRunner.run(test)
