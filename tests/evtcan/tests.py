from gateway.evtcan.device_construct import MessageBox, DeviceConstruct
from gateway.evtcan.controller import EvtCanMessage
import unittest
import struct

class TestDeviceConstruct(unittest.TestCase):
    def setUp(self):
        self.construct = DeviceConstruct("INTEL_EVT_CAN.dbc")
    def tearDown(self):
        pass
    def test_devices(self):
        device = self.construct.fetchDevice('BMS0')
        self.assertIsNotNone(device.messageBox.messages['BMS0_temp1'].Cell_temp1)

    def test_Signalfunctions(self):
        #Big Endian"""
        #databyteRaw = b'\x00\x04\x00\x03\x00\x02\x00\x01'
        #Little Endian"""
        #databyteRaw = b'\x00\x00\x00\x00\x04\x03\x02\x01'
        databyteRaw = b'\x01\x02\x03\x04\x05\x06\x78\xF0'
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
        # print(message.Module_V1)
        # print(message.Module_V2)
        # print(message.Module_V3)
        # print(message.Module_V4)
        # print(message.Module_V5)

    def test_Discharges(self):
        device = self.construct.fetchDevice('BMS0')
        databyteRaw = b'\x00\x68\x00\x4E\xA6\xE1\x0F\xA0'

        message = EvtCanMessage(device.messageBox.messages['BMS0_module_discharge'], databyteRaw)

    def test_unsignedSingal(self):
        pass
        #282
        #19 00 85 00 DF FF
        # Yaw Y -33
