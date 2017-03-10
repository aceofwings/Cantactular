class Listener:

    def __init__(self):
        self.handlers = {}

    def addHandler(canid, handler):
        if canid in handlers:
            handlers[canid].append(handler)
        else:
            handlers[canid] = []
            handlers[candid].append(handler)

    def removeHandler(canid,handler):
        pass

    def notify(self,canmessage):
        for handler in handlers[canmessage.canid]
            handler(canmessage.canid,canmessage.data)
