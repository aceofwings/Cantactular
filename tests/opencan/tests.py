import unittest
from gateway.opencan.sdo import SDO
from gateway.can.device import CanOpenDevice

class TestSDO(unittest.TestCase):
    def setUp(self):
        self.device = CanOpenDevice(2, 'MotorController')
        self.sdo = SDO(self.device)
    def tearDown(self):
        pass
    def test_SDO_read(self):
        print('\nTesting Read() which writes SDO to nodeID ')
        a = self.sdo.read(0x2159, 0x05)
        print(a)
