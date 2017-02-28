from gateway.can.interface import Interface
from gateway.can.message import CanMessage
from sys import platform
import unittest
import socket

class TestInterface(unittest.TestCase):
    def setUp(self):
        self.test_address = "vcan0"
        self.test_listeners = []
        self.test_interface = Interface(self.test_address, self.test_listeners)
        self.test_message = CanMessage().create(4759, '8F7D1A2B')

    def tearDown(self):
        self.test_interface.close()

    def test_startSocket(self):
        result = self.test_interface.start()
        self.assertTrue(result)

#         #Should throw socket.error when interface name not present on device list
        with self.assertRaises(socket.error):
            err_interface = Interface('wuiheoigrog34', [])
            err_interface.start()
            #raise OSError('e')

    def test_write(self):
        result = self.test_interface.write(self.test_message)
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
