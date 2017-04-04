from gateway.evtcan.device_construct import MessageBox, DeviceConstruct
import unittest

class TestDeviceConstruct(unittest.TestCase):
    def setUp(self):
        self.construct = DeviceConstruct("test_EVT_CAN.dbc")
    def tearDown(self):
        pass
    def test_devices(self):
        print("Fetching Device\n")
        self.construct.fetchDevice('BMS')

    def test_index(self):
        pass
        #self.assertEqual(self.obj[0x1018].parametername, "Identity object")
    def test_SubIndex(self):
        pass
        #elf.assertEqual(self.obj[0x1018][0x0].parametername, "Number of entries")

if __name__ == '__main__':
    unittest.main()
