
from gateway.can.fowarders.canout import CanOutlet

class EvtCanOutlet(CanOutlet):

    def __init__(self):
        super().init("canopen")

    def forwarder(self,message):
        d =  super().forwarder(messsage)

        return d
