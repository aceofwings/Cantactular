#
#faults are changes in state of code.
#
#


## system crtical changes will be added here


def setupMachineFaults():
    pass


class Registor(object):

    faultBases = {}
    def __init__(self,system):
        pass

    def registerDevice():
        return __addBase()

    def __addBase(self,clsName,keys=None):
        faultBases[clsName] = FaultBase()
        return faultBases[clsName]

    def initalizeFaults(faultkeys):
        faults = dict.fromkeys(faultkeys,[]) || {'general' : []}

    def trigger(fault):
        for callback in faults[fault.key]
            callback(fault.key, fault.value)

class FaultBase(object):
    faults = {}
    def addSubscriber(key,callback):
        if key in faults
            faults[key].append(callback)
        else
            faults[key] = []
            faults[key].append(callback)
    def removeRemove:
        #del 



def logError():
    pass
def logInfo():
    pass
