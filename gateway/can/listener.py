import logging
#
#
#
#
class Listener:
    def __init__(self):
        self.listening = {}
        self.handlers = {}
    def addHandler(self,canid, handler):
        if canid in self.handlers:
            self.handlers[canid].append(handler)
        else:
            self.handlers[canid] = []
            self.handlers[canid].append(handler)

    def removeHandler(self,canid,handler):
        pass

    def _notify(self,canmessage):
        self._notifyAll(canmessage)
        if not self.handlers or not canmessage.canid in self.handlers:
            return
        else:
            self.notify(canmessage)


    def _notifyAll(self,canmessage):
        if 'all' in self.handlers:
            for handler in self.handlers['all']:
                self.notifyAll(canmessage)

    def notify(self,canmessage,**KWARGS):
        for handler in self.handlers[canmessage.canid]:
            handler(canid=canmessage.canid, message=canmessage, **KWARGS)

    def notifyAll(self,canmessage,**KWARGS):
        for handler in self.handlers['all']:
            handler(canid=canmessage.canid,message=canmessage, **KWARGS)
