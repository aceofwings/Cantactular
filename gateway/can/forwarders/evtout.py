
from gateway.can.forwarders.canout import CanOutlet

class EvtCanOutlet(CanOutlet):

    def __init__(self,engine):
        super().init("canopen")

    def deconstruct_can_message(self,message):
        d =  super().forwarder(messsage)
        d['type'] = self.base
        return d
