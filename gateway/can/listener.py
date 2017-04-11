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
        if not self.handlers or not canmessage.canid in self.handlers:
            if 'all' in self.handlers:
                self.notifyAll(canmessage)
            return
        else:
            self.notify(canmessage)



    def notify(self,canmessage):
        for handler in self.handlers[canmessage.canid]:
            handler(canmessage.canid,canmessage.data)

    def notifyAll(self,canmessage):
        for handler in self.handlers['all']:
            handler(canmessage.canid,canmessage.data)
