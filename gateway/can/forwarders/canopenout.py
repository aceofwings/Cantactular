from gateway.can.forwarders.canout import CanOutlet

class CanOpenOutlet(CanOutlet):

    def __init__(self,engine):
        super().init("evt",engine)

    def deconstruct_can_message(self,message):
        d = super().deconstruct_can_message(messsage)
        d['type'] = self.base
        return d
