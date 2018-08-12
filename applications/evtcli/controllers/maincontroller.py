from lib import evtcurses
from gateway.can.controllers.base import BaseController
from lib.evtcurses import ScreenObject, screenObjects, appendToScreenObjects, ORANGE
from gateway.core.service import Service
from threading import Thread
import curses

class MainController(BaseController):

    def __init__(self):
        evt = ScreenObject(0,0 ,"EVT")
        evt.data = " CLI VERSION 1.0.0 "
        evt.colorPair = 209
        screenObjects.append(evt)
        service = Service(target=evtcurses.startCurses,clean_up=self.end)
        service.start()

    def end(self):
        print("ended")
