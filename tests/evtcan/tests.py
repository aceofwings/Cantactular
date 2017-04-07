from gateway.evtcan.device_construct import MessageBox, DeviceConstruct
from gateway.evtcan.controller import EvtCanMessage
import unittest
import struct

class TestDeviceConstruct(unittest.TestCase):
    def setUp(self):
        self.construct = DeviceConstruct("test_EVT_CAN.dbc")
    def tearDown(self):
        pass
    def test_devices(self):
        device = self.construct.fetchDevice('BMS')
        self.assertIsNotNone(device.messageBox.messages['BMS_data3'].Cell_V10)

    def test_Signalfunctions(self):
        #58464568856d6244
        #0101 1000 0100 0110 0100 0101 0110 1000 1000 0101 0110 1101 0110 0010 0100 0100
        #101100001000110010001010110100010000101011011010110001001000100
        #
        """Little Endian
        This may be the right scheme but we will see soon with firmware tests
        """
        databyteRaw = b'\x00\x04\x00\x03\x00\x02\x00\x01'
        """Big Endian"""
        #databyteRaw = b'\x01\x00\x02\x00\x01\x00\x01\x00'

        device = self.construct.fetchDevice('BMS')
        #
        message = EvtCanMessage(device.messageBox.messages['BMS_data3'], databyteRaw)

        #self.assertEqual(message.Cell_V9,0x1)
        #self.assertEqual(message.Cell_V10,0x2)
        #self.assertEqual(message.Cell_V11,0x1)
        #self.assertEqual(message.Cell_V11,0x1)




if __name__ == '__main__':
    unittest.main()
