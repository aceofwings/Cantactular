import tests.objectdictionary.test as objtest
import unittest
def run():
    suite = unittest.TestLoader().loadTestsFromTestCase(objtest.TestObjectDictionary)
    unittest.TextTestRunner(verbosity=2).run(suite)
