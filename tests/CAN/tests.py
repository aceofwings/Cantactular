import unittest

#NOTE by providing a load_tests() function will be called to help load anything
#from the subdirectories.
#


#
#Load test from subpackages
#
def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    return suite
