from gateway.can.controller import Controller
import unittest

class TestCanMessage(unittest.TestCase):
	def setUp(self):
		self.controller = Controller()
		self.controller.addInterface("vcan0")

	def tearDown(self):
		pass


if __name__ == '__main__':
    unittest.main()
