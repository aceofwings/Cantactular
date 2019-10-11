# from gateway.utils.objectdictionary import ObjectDictionary
# import unittest
#
# class TestObjectDictionary(unittest.TestCase):
#     def setUp(self):
#         self.obj = ObjectDictionary.initialize('MotorController.eds')
#     def tearDown(self):
#         pass
#     def test_ReadEdsFile(self):
#         self.assertNotEqual(self.obj, None)
#     def test_index(self):
#         self.assertEqual(self.obj[0x1018].parametername, "Identity object")
#     def test_SubIndex(self):
#         self.assertEqual(self.obj[0x1018][0x0].parametername, "Number of entries")
#
# if __name__ == '__main__':
#     unittest.main()
