from gateway.can.traffic.message import CanMessage
import unittest
import time

class TestCanMessage(unittest.TestCase):

    def setUp(self):
        self.msg = CanMessage(**{'canid' : 1, 'dlc' : 0, 'data' : b'@\x18\x10\x02\x02\x00\x00\x00', 'received' : time.time(), 'type': "EVT"})
        self.msgtwo = CanMessage(**{'canid' : 1, 'dlc' : 4, 'data' : b'@\x18\x10\x02\x02\x00\x00\x00', 'received' : time.time(), 'type': "EVT"})
        self.test_from_json_string = "{\"canid\": 1, \"dlc\": 4, \"received\": 1512076189.803494, \"type\": \"OPENCAN\", \"data\": [64, 24, 16, 2, 2, 0, 0, 0]}"
    def test_base_attributes(self):
        self.assertTrue(self.msg.canid == 1)
        self.assertTrue(self.msg.dlc == 0)
        self.assertTrue(self.msg.type == "EVT")

    def test_to_json(self):
        pass
    
    def test_from_json(self):
        m = CanMessage.from_JSON(self.test_from_json_string)
        self.assertTrue(m.canid == 1)
        self.assertTrue(m.dlc == 4)
        self.assertTrue(m.type == "OPENCAN")

    def tearDown(self):
        pass
