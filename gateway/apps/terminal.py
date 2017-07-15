
from gateway.opencan.opencancontroller import CanOpenController
from gateway.evtcan.controller import EvtCanController
from gateway.can.device import CanOpenDevice
from gateway.settings.loader import buildController
from gateway.core.systemlogger import logger
import curses
import signal
import sys
#may want to inherit from our own custom code
class Terminal(object):

    def __init__(self):
        super()
        term = TermEvtCanController("INTEL_EVT_CAN.dbc")
        canopen = TermOpenController()

        #term = TermOpenController()
        buildController(term)
        buildController(canopen)

        while True:
            pass

        #canopen.motor.sdo.write_values[0x2220] = number

    def start(self):
        pass

    def handleWrite(self, **kwargs):
        message = kwargs['message']
        self.data = message.data

    def close(self, signum, frame):
        curses.nocbreak()
        self.screen.keypad(0)
        curses.echo()
        curses.endwin()
        sys.exit(1)

class TermEvtCanController(EvtCanController):

    def buildController(self):
        super().buildController()
        self.setupListener()
        self.addDevice(self.devices.fetchDevice("BMS0"))
        self.addDevice(self.devices.fetchDevice("BMS1"))
        self.addDevice(self.devices.fetchDevice("BMS2"))
        self.addDevice(self.devices.fetchDevice("BMS3"))
        self.controllerListener.addHandler('all',self.handleBroadCast)
        return True

    def handleBroadCast(self, canid, message, **kwargs):
        logger.debug("%s", kwargs['evtmessage'])


class TermOpenController(CanOpenController):

    def __init__(self):
        super().__init__()
        #self.controllerListener.addHandler(0x00,self.handleBroadCast)

    def buildController(self):
        super().buildController()
        self.motor = CanOpenDevice(0x01,"MotorController.eds")
        self.addDevice(self.motor)
        return True
