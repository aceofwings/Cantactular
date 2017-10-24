
from gateway.can.forwarders.canout import CanOutlet

class EvtCanOutlet(CanOutlet):

    def __init__(self,engine):
        super().init(engine,message_type="evt")

    def deconstruct_can_message(self,message):
        d =  super().deconstruct_can_message(message)
        d['type'] = self.base
        return d
