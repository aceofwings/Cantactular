#
#faults are changes in state of code.
#
#


## system crtical changes will be added here


def setupMachineFaults():
    pass


class RegistorFault(object):

    def __init__(self,system):
        pass
    def addFaultListener(key='general',callback):
        pass
    def removefaultListener(key='general',callback):
        pass

    def registerFault(self,fault):
        pass


class Fault(object):
    def __init__(key='general', value):
        self.key
        self._value
    @property
    def value(self):
        return self.__value
    @value.setter
    def setValue(self,value)
        self.__value = value
        self._notify()
    def _notify(self):
        self.registerFault(self)


def logError():
    pass
def logInfo():
    pass
