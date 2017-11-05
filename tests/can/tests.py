import unittest
from gateway.can.engine import Engine

class TestEngine(unittest.TestCase):

    def setUp(self):
        self.rx_core = b'{"message": {"canid": 1, "data": [0, 0, 0, 0, 0, 0, 0, 0], "dlc": 1}, "type": "EVTCAN", "recieved": 234.000079}'

    def test_json_encode(self):
        pass


    def test_json_decode(self):
        pass

    def test_bytes_to_json(self):
        print(Engine().COREreceive(self.rx_core))
