import unittest
from gateway.core.application import Application
from gateway.evtcan.dbcParser import CANDatabase
from gateway.evtcan.device_construct import DeviceConstruct

class TestApplicationCore(unittest.TestCase):

    def setUp(self):
        pass#self.app = Application()
    def test_load_application_handlers(self):
        pass
class TestDbcParser(unittest.TestCase):

    def setUp(self):
        self.db = CANDatabase('INTEL_EVT_CAN.dbc')
        self.db.Load()

    def test_txNode_exists(self):
        """Check to see wether BMS0 is in the parse DBC file"""
        self.assertTrue('BMS0' in self.db._txNodes)

    def test_messsages_exists(self):
        self.assertTrue(len(self.db._txNodes['BMS0']))

class TestDeviceConstruct(unittest.TestCase):
    def setUp(self):
        self.dc = DeviceConstruct('INTEL_EVT_CAN.dbc')
    def test_load_application_handlers(self):
        self.dc.fetchDevice('BMS0').messages[136](500)
    def test_master_message_box(self):
        pass
