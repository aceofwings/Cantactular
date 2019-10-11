# import unittest
# from gateway.opencan.sdo import SDO
# from gateway.can.device import CanOpenDevice
# from gateway.can.message import CanMessage
# from gateway.settings.loader import buildController
# from gateway.opencan.sdologger import SDOLog
# from tests.opencan.canopentestcontroller import TestController
# import time
#
#
# class TestSDO(unittest.TestCase):
#     def setUp(self):
#         self.controller = TestController()
#         buildController(self.controller)
#         self.log = SDOLog()
#         #self.device = CanOpenDevice(2, 'MotorController')
#         #self.sdo = SDO(self.device)
#     # def tearDown(self):
#     #     pass
#     # def test_SDO_read(self):
#     #     print('\nTesting Read() which reads from nodeID Object Dictionary')
#     #     a = self.sdo.read(lambda m: print("handled"+m), 0x1801, 0x3)
#     # def test_SDO_write(self):
#     #     print('\nTesting Write() which writes data to nodeID Object Dictionary')
#     #     a = self.sdo.write(lambda m: print("handled"+m), 0x3FE, 0x1801, 0x3)
#     # def test_SDO_xreceive(self):
#     #     print('\nTesting receive listener notify to handle callbacks')
#     #     a = self.sdo.write(lambda m: print("handled data: "+m), 0x3FE, 0x1801, 0x3)
#     #     d = [0x60, 0x01, 0x18, 0x03, 0xA7, 0x0, 0x00, 0xB9]
#     #     m = CanMessage.create(0x582, ''.join('%02x' % x for x in d))
#     #     self.sdo._receiveResponse(m)
#
#     def test_sdo_log(self):
#         self.controller.motor.sdo.read(self.log.handle, 0x2511, 5)
#         time.sleep(30)
# #cansend 581#6018100400000000
