import unittest
import json

from gateway.can.engine import Engine
from gateway.can.handler import BasicMessageHandler,BaseMessageTypes
class TestEngine(unittest.TestCase):

    def setUp(self):
        self.rx_core = b'{"message": {"canid": 1, "data": [0, 0, 0, 0, 0, 0, 0, 0], "dlc": 1}, "type": "EVTCAN", "recieved": 234.000079}'
        self.handler = BasicMessageHandler(Engine())
        self.decoded_msg = json.loads(self.rx_core.decode())
    def test_json_encode(self):
        pass


    def test_json_decode(self):
        pass

    def test_bytes_to_json(self):
        """see if message can be decoded and properly navigated with hash notation"""
        self.assertEqual(Engine().COREreceive(self.rx_core)['message']['canid'], 1)

    def test_baseMessageTypeConversion(self):
        """Check to see if message type is coverted by handler correctly"""
        self.assertIs(BaseMessageTypes.EVTCAN, self.handler._msg_type_compose(self.decoded_msg['type']))
