#
#
#
#
#
#
#
#
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

    def notify(self,canmessage):
        for handler in self.handlers[canmessage.canid]:
            handler(canmessage.canid,canmessage.data)
