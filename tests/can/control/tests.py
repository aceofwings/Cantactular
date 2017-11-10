import unittest

from gateway.can.control.noticehandler import NoticeHandler
from gateway.can.control import notices
from gateway.can.engine import Engine
class TestNotice(unittest.TestCase):

    def setUp(self):
        self.NT = NoticeHandler(Engine())

    def test_simpleNoticeHandle(self):
        #self.NT.recoverySucessFull(notices.RecoverySucessFull())
        print(self.NT._noticers)
        #self.NT.handle_notice(notices.RecoverySucessFull())
    def tearDown(self):
        pass
