import unittest
import os
from gateway.utils.resourcelocator import ResourceLocator

class TestResourceLocator(unittest.TestCase):
    def setUp(self):
        self.locator = ResourceLocator.get_locator()
        self.relative_locator = ResourceLocator.get_locator('gateway')

    def tearDown(self):
        pass

    def test_resourceLocatorRootPath(self):
        """Test to see if class locaor ROOT_PATH is set"""
        self.assertIsNotNone(self.locator.ROOT_PATH, msg="root_path does not exist")

    def test_relative_path(self):
        """Test to see if a relative path can be defined correctly"""
        absolute_path = os.path.join(self.locator.ROOT_PATH, 'gateway')
        self.assertEqual(absolute_path, self.relative_locator.ROOT_PATH, msg="Paths are not equal")
