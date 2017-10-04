import os
import unittest
from gateway.utils.resourcelocator import ResourceLocator
from unittest import TestLoader

TEST_PATH = "tests"

verbosity = 1

test_loader = unittest.defaultTestLoader


def find_test_modules(test_modules=None):
    test_locator = ResourceLocator.get_locator(TEST_PATH)
    test_suite = test_loader.discover(test_locator.ROOT_PATH)
    return test_suite

def run_tests(test_classes=None):
    test_runner = unittest.TextTestRunner(verbosity=verbosity)
    if test_classes:
        suite = load_test_from_classes(test_classes)
        if not suite.countTestCases():
            return -1
        else:
            test_runner.run(suite)
            return 0


    tests = find_test_modules(test_modules)
    test_runner.run(tests)
    return 0

def load_test_from_classes(class_names):
    test_locator = ResourceLocator.get_locator(TEST_PATH)
    test_suite = test_loader.discover(test_locator.ROOT_PATH)
    temp_ts = unittest.TestSuite()
    for test in test_suite:
        suite = test.__dict__["_tests"]
        if len(suite):
            for case in suite:
                if case.__dict__["_tests"][0].__class__.__name__ in class_names:
                    temp_ts.addTest(case)
    return temp_ts


def load_module_test_case(module_name):
    return test_loader.loadTestsFromName(module_name)
