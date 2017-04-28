
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
        #term = TermOpenController()
        buildController(term)
        self.screen = curses.initscr()
        self.screen.keypad(1)
        signal.signal(signal.SIGINT, self.close)
        number = 0
        curses.noecho()

        self.temps = {}
        term.controllerListener.addHandler(0x80,self.update)
        term.controllerListener.addHandler(0x81,self.update)
        term.controllerListener.addHandler(0x100,self.update)
        term.controllerListener.addHandler(0x101,self.update)
        term.controllerListener.addHandler(0x180,self.update)
        term.controllerListener.addHandler(0x181,self.update)
        term.controllerListener.addHandler(0x200,self.update)
        term.controllerListener.addHandler(0x201,self.update)
        while 1:
            n = 0
            for key in self.temps.keys():
                for x in range(0, len(self.temps[key].signals)):
                    self.screen.addstr(n, x*2+5, "Temps: " + str(self.temps[key]))
                n+=1

            self.screen.refresh()

        #term.motor.sdo.write_values[0x2220] = number

    def start(self):
        pass

    def update(self,nodeid, evtMessage):
        self.temps[nodeid] = evtMessage

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
        self.motor = CanOpenDevice(0x01,"MotorController")
        self.addDevice(self.motor)
        return True

    def handleBroadCast(self,nodeID,value):
        print("Handle BroadCast")
