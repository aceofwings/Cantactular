from gateway.can.message import CanMessage
import unittest
import struct

class TestCanMessage(unittest.TestCase):
    def setUp(self):
        self.test_frame = b'\x00\x01\x00\x02\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00'
        self.test_message = CanMessage(self.test_frame)
    def tearDown(self):
        pass
    def test_DataLength(self):
        self.assertEqual(self.test_message.datalen, 0)
    def test_CanId(self):
        self.assertEqual(self.test_message.canid, 65538)
    def test_Data(self):
        self.assertEqual(self.test_message.data, (0, 0, 0, 0, 0, 0, 0, 0))
    def test_MessagetoBytes(self):
        canid = 420
        data = 'DEADBEEF'
        databytes = b'\xde\xad\xbe\xef\x00\x00\x00\x00'
        test_message = CanMessage().create(canid, data)
        bytes = test_message.bytes()

        can_frame = struct.Struct('>IB3x8s')
        unpackedmsg = can_frame.unpack(bytes)

        datalen = len(bytearray.fromhex(data))

        self.assertEqual(canid, unpackedmsg[0])
        self.assertEqual(datalen, unpackedmsg[1])
        self.assertEqual(databytes, unpackedmsg[2])


if __name__ == '__main__':
    unittest.main()
