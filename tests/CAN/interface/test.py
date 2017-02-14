from gateway.CAN.interface import Interface
from sys import platform
import unittest

class TestCanMessage(unittest.TestCase):
	def setUp(self):
		self.test_address = "can0"
		self.test_interface = Interface(self.test_address)

	def tearDown(self):
		pass
	def test_startSocket(self): #add assert cases **Need Linux
		test_interface.start(self)
	def test_closeSocket(self): #add assert cases **Need Linux
		test_interface.close(self)
    


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

    