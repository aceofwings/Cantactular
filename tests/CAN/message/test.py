from gateway.can.message import CanMessage
import unittest

class TestCanMessage(unittest.TestCase):
    def setUp(self):
        self.test_frame = b'\x00\x01\x00\x02\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00'
        self.test_message = CanMessage(self.test_frame)
    def tearDown(self):
        pass
    def test_DataLength(self):
        self.assertEqual(self.test_message.datalen, 0)
    def test_CanId(self):
        self.assertEqual(self.test_message.canid, 33554688)
    def test_Data(self):
        self.assertEqual(self.test_message.data, (0, 0, 0, 0, 0, 0, 0, 0))
    def test_toString(self):
        self.assertEqual(str(self.test_message), "id:0x2000100 datalen: 0x0 ::data::(0, 0, 0, 0, 0, 0, 0, 0)")


if __name__ == '__main__':
    unittest.main()
