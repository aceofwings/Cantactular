from gateway.can.forwarders.canout import CanOutlet

class CanOpenOutlet(CanOutlet):

    def __init__(self,engine):
        super().init(engine,message_type="canopen")

    def deconstruct_can_message(self,message):
        d = super().deconstruct_can_message(message)
        return d
