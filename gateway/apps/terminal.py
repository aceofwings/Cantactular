
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

        self.screen = curses.initscr()
        self.screen.keypad(1)
        self.screen.nodelay(1)
        signal.signal(signal.SIGINT, self.close)
        curses.noecho()
        curses.cbreak()

        write_value = 0
        old_value = 0
        self.data = 0

        while True:

            values = canopen.motor.values.copy()

            new_press = self.screen.getch()
            if new_press == 261:#259 up
                write_value += 1
            if new_press == 260:#258 down
                write_value -= 1

            values['write_response'] = self.data
            values['write_value'] = write_value
            values['write_times'] = canopen.motor.sdo.write_times
            if write_value != old_value:
                canopen.motor.sdo.write_values[0x2220] = write_value
                #canopen.motor.sdo.write(self.handleWrite, write_value, 0x2220)
                old_value = write_value

            self.screen.clear()
            row = 0
            for key in values.keys():
                log = str(key)+' : '+str(values[key])
                self.screen.addstr(row, 0, str(key)+' : '+str(values[key]))
                row = row + 1
            self.screen.refresh()

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

    def handleBroadCast(self,nodeID, evtMessage):
        logger.debug("%s",evtMessage)


class TermOpenController(CanOpenController):

    def __init__(self):
        super().__init__()
        self.controllerListener.addHandler(0x00,self.handleBroadCast)

    def buildController(self):
        super().buildController()
        self.motor = CanOpenDevice(0x01,"MotorController.eds")
        self.addDevice(self.motor)
        return True

    def handleBroadCast(self,nodeID,value):
        print("Handle BroadCast")
