from  gateway.core.systemlogger  import RunRotatingtHandler, logger
from gateway.evtcan.device_construct import DeviceConstruct
from gateway.can.message import EvtCanMessage
import unittest
import json

class TestCore(unittest.TestCase):
    def setUp(self):
        logger.debug("testing json dump")
        self.parsed =  {"Battery1":  128 ,"Battery1":  100 ,"Battery2":  200 ,"Battery3":  300,"Battery4":  500}
        self.construct = DeviceConstruct("INTEL_EVT_CAN.dbc")



    def test_dumpJson(self):
        databyteRaw = b'\x01\x02\x03\x04\x05\x06\x78\xF0'
        device = self.construct.fetchDevice('BMS0')
        message = EvtCanMessage(device.messageBox.messages['BMS0_temp1'], databyteRaw)
        logger.debug(json.dumps(self.parsed))
        logger.debug(json.dumps(message.contents()))
    def tearDown(self):
        pass
