import unittest
import tests.objectdictionary.test as objtest
from gateway.utils.testfinder import TestFinder

finder = TestFinder
finder.loadTestFiles()


def findTestModules():
    pass
