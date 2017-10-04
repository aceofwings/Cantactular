import os
import unittest
from gateway.utils.resourcelocator import ResourceLocator
from unittest import TestLoader

TEST_PATH = "tests"

def find_test_modules():
    test_loader = unittest.defaultTestLoader
    test_locator = ResourceLocator.get_locator(TEST_PATH)
    test_suite = test_loader.discover(test_locator.ROOT_PATH)
    return test_suite


def run_tests(verbose=0,test_modules=None):
    test_runner = unittest.TextTestRunner(verbosity=verbose)
    tests = find_test_modules()
    test_runner.run(tests)

def load_module_test_Case(modulename):
    TestLoader.loadTestsFromName(modulename)
