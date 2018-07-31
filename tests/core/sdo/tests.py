import unittest
import os
from gateway.can.sdo.message import SdoMessage
from gateway.can.sdo.message import CommandByte
class TestSdoMessage(unittest.TestCase):
    def setUp(self):
        self.sdoMessage = SdoMessage.getMessege(0x1018,0x01,0x00)
        self.anotherMessage = SdoMessage.getMessege(0x2220,0x00,0x00)

        self.rawUpload = b'@\x18\x10\x02\x02\x00\x00\x00\x00\x00\x00\x00'
        self.rawDownload = b'+\x18\x10\x01\x00\x00\x00\x00\x00\x00\x00\x00'

    def tearDown(self):
        pass
    def test_toBytes(self):
        """Translate the SDO message correctly"""
        pass
    def test_init(self):
        """See if intialize will have correct default value"""
        pass
