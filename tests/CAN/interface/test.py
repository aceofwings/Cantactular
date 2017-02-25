from gateway.can.interface import Interface
from gateway.can.message import CanMessage
from sys import platform
import unittest
import socket

class TestInterface(unittest.TestCase):

	def setUp(self):
		self.test_address = "vcan0"
		self.test_interface = Interface(self.test_address)
        self.test_message = CanMessage().create(43578,'Test can message for testing interface')

	def tearDown(self):
		self.test_interface.close()

	def test_startSocket(self):
		result = test_interface.start(self)
        self.assertTrue(result)

        #Should throw socket.error when interface name not present on device list
        with self.assertRaise(socket.error):
            err_interface = Interface('wuiheoigrog34')
            err_interface.start()

    def test_write(self):
        result = self.test_interface.write(test_message)
        self.assertNotEqual(result, 0)



if __name__ == '__main__':
	if platform == "linux" or platform == "linux2":
		# linux
		print(platform, "is okay to run this test.")
		unittest.main()
	elif platform == "darwin":
		# OS X
		print(platform, "- Mac OSX is unable to run this test. Requires linux.")
	elif platform == "win32":
		# Windows...
		print(platform, "- Windows is unable to run this test. Requires linux.")
	else:
		print(platform, "is unable to run this test. Requires linux.")
