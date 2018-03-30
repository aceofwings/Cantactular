import os
import unittest
from gateway.utils.resourcelocator import ResourceLocator
from unittest import TestLoader

TEST_PATH = "tests"
verbosity = 1
test_loader = unittest.defaultTestLoader


def find_test_modules(file_pattern='test*.py'):
    test_locator = ResourceLocator.get_locator(TEST_PATH)
    test_suite = test_loader.discover(test_locator.ROOT_PATH, pattern=file_pattern)
    return test_suite

def run_tests(test_classes=None):
    """
    run_tests - runs a test suite with specified paramters
    :param test_classes: list of tests classnames to only test
    :return int: -1 for failure or 0 for success
    """
    test_runner = unittest.TextTestRunner(verbosity=verbosity)

    if test_classes is not None:
        suite = load_test_from_classes(test_classes)
        if not suite.countTestCases():
            return False
        else:
            test_runner.run(suite)
            return True

    tests = find_test_modules()
    test_runner.run(tests)
    return True

def load_test_from_classes(class_names):
    """
    load_test_from_classes - returns a suite with specified class_names
    :param class_names: list of tests classnames to add to the suite
    """
    test_suite = find_test_modules()
    temp_ts = unittest.TestSuite()
    for test in test_suite:
        suite = test.__dict__['_tests']
        if len(suite):
            for case in suite:
                if case.__dict__['_tests'][0].__class__.__name__ in class_names:
                    temp_ts.addTest(case)
    return temp_ts
