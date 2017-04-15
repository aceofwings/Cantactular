from gateway.evtcan.device_construct import MessageBox, DeviceConstruct
from gateway.evtcan.controller import EvtCanMessage
import unittest
import struct

class TestDeviceConstruct(unittest.TestCase):
    def setUp(self):
        self.construct = DeviceConstruct("EVT_CAN.dbc")
    def tearDown(self):
        pass
    def test_devices(self):
        device = self.construct.fetchDevice('BMS0')
        self.assertIsNotNone(device.messageBox.messages['BMS0_temp1'].Cell_temp1)

    def test_Signalfunctions(self):
        #58464568856d6244
        #0101 1000 0100 0110 0100 0101 0110 1000 1000 0101 0110 1101 0110 0010 0100 0100
        #101100001000110010001010110100010000101011011010110001001000100
        #
        """Little Endian
        This may be the right scheme but we will see soon with firmware tests
        """
        #databyteRaw = b'\x00\x04\x00\x03\x00\x02\x00\x01'
        """Big Endian"""
        databyteRaw = b'\x00\x00\x00\x00\x04\x03\x02\x01'

        device = self.construct.fetchDevice('BMS0')

        message = EvtCanMessage(device.messageBox.messages['BMS0_temp1'], databyteRaw)
        self.assertEqual(message.Cell_temp1,0x1)
        self.assertEqual(message.Cell_temp2,0x2)
        self.assertEqual(message.Cell_temp3,0x3)
        self.assertEqual(message.Cell_temp4,0x4)

    def test_SignalVoltages(self):
        device = self.construct.fetchDevice('BMS0')
        databyteRaw = b'\x00\x68\x00\x4E\xA6\xE1\x0F\xA0'
        message = EvtCanMessage(device.messageBox.messages['BMS0_module_voltages1'], databyteRaw)
        print(bin(message.data))
        print(message.Module_V1)
        print(message.Module_V2)





if __name__ == '__main__':
    unittest.main()
