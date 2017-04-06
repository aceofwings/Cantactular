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
        databyteRaw = b'\x56\x46\x45\x68\x85\x62\x64\x44'
        databyteRaw = b'\x01\x00\x00\x00\x00\x00\x00\x00'
        device = self.construct.fetchDevice('BMS')

        message = EvtCanMessage(device.messageBox.messages['BMS_data3'], databyteRaw)
        print("\ncells Voltage is " + str(message.Cell_V9))
        print(bin(message.data))



if __name__ == '__main__':
    unittest.main()
