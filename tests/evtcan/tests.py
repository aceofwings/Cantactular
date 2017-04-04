from gateway.evtcan.device_construct import MessageBox, DeviceConstruct
import unittest

class TestObjectDictionary(unittest.TestCase):
    def setUp(self):
        construct = DeviceConstruct("test_EVT_CAN.dbc")
    def tearDown(self):
        pass
    def test_MessageBoxSignals(self):
        print("HELLLO")
        #self.assertNotEqual(self.obj, None)
    def test_index(self):
        pass
        #self.assertEqual(self.obj[0x1018].parametername, "Identity object")
    def test_SubIndex(self):
        pass
        #elf.assertEqual(self.obj[0x1018][0x0].parametername, "Number of entries")

if __name__ == '__main__':
    unittest.main()
