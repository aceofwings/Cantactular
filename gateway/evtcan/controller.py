from gateway.can.controller import Controller
from gateway.can.listener import Listener
from gateway.can.message import EvtCanMessage
from gateway.evtcan.evt_listener import EvtCanListener
from gateway.evtcan.device_construct import DeviceConstruct
from gateway.evtcan.dbcParser import CANDatabase

class EvtCanController(Controller):

    def __init__(self,dbcFile):
        super().__init__()
        self.devices = DeviceConstruct(dbcFile)
        self.CANDatabase = self.devices.fetchDatabase()
        self.controllerListener = EvtCanListener()

    def addDevice(self,device):
        super().addDevice(device)
        self.controllerListener.messages.update(device.listener.messages)
