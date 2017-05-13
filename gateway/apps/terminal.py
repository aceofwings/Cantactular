
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
        self.evtterm = EvtTerminalControl("INTEL_EVT_CAN.dbc")
        self.openterm = OpenTerminalControl()

        #term = TermOpenController()
        buildController(self.evtterm)
        buildController(self.openterm)

        self.screen = curses.initscr()
        self.screen.keypad(1)
        self.screen.nodelay(1)
        signal.signal(signal.SIGINT, self.close)
        curses.noecho()
        curses.cbreak()

        self.start()

    def start(self):
        self.throttle_write_value = 0
        self.old_throttle_value = 0
        self.throttle_index = 0x2220

        while True:
            self.update()

    def close(self, signum, frame):
        curses.nocbreak()
        self.screen.keypad(0)
        curses.echo()
        curses.endwin()
        sys.exit(1)

    def update(self):
        values = self.canopen.motor.values.copy()

        new_press = self.screen.getch()
        if new_press == 261:#259 up
            self.throttle_write_value += 1
        if new_press == 260:#258 down
            self.throttle_write_value -= 1

        #values['throttle_write_value'] = self.throttle_write_value
        #values['throttle_write_times'] = self.canopen.motor.sdo.throttle_write_times

        if self.throttle_write_value != self.old_throttle_value:
            self.openterm.motor.sdo.write_values[self.throttle_index] = self.throttle_write_value
            self.old_throttle_value = self.throttle_write_value

        self.screen.clear()

        row = 0
        for key in values.keys():
            self.screen.addstr(row, 0, str(key)+' = '+str(values[key])
            row = row + 1

        self.screen.refresh()




class EvtTerminalControl(EvtCanController):

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


class OpenTerminalControl(CanOpenController):

    def __init__(self):
        super().__init__()
        #self.controllerListener.addHandler(0x00,self.handleBroadCast)

    def buildController(self):
        super().buildController()
        self.motor = CanOpenDevice(0x01,"MotorController.eds")
        self.addDevice(self.motor)
        return True
