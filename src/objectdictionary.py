import collections, configparser

class DictObj():
    index = 0x0
    ParameterName = ''
    ObjectType = 0

    def __init__(self, index, parameterName, objectType):
        self.index = index
        self.ParameterName = parameterName
        self.ObjectType = objectType

class ObjectDictionary(collections.Mapping):

    def __init__(self):
        self.names = {}
        self.ids = {}

    @classmethod
    def initialize(self, edsPath):
        dic = ObjectDictionary()
        eds = configparser.ConfigParser()
        eds.read(edsPath)
        for section in eds.sections():


    def __setitem__(self,key,value):
        pass

    def __getitem__(self,key):
        pass

    def __iter__():
        pass

    def __len__():
        pass



if __name__ == '__main__':
    cow = ObjectDictionary.initialize('..\edsfiles\MotorController.eds')
