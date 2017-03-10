#
#faults are changes in state of code.
#
#


## system crtical changes will be added here

class Registor(object):

    faultBases = {}

    def registerBase(self,faultBase):
        keyName = faultBase.__class__.__name__
        self.faultBases[keyName] = faultBase
        return faultBases[clsName]

    def faultFire(self,fault):
        print("Fault fired" + fault.__class__)

    def initalizeFaults(faultkeys):
        faultBases = dict.fromkeys(faultkeys,[]) || {'general' : []}


class FaultBase(object):
    def __init__(self,registor):
        self.registor = registor
        self.callbacks = {}

    def addSubscriber(key,callback):
        if key in faults
            callbacks[key].append(callback)
        else
            callbacks[key] = []
            callbacks[key].append(callback)
    def notify(key,value):
        for callback in callbacks[key]
            callback(value)
            self.registor.faultFire(self)
