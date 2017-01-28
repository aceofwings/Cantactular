import collections, configparser

class DictObj():
    index = 0x0
    ParameterName = ''
    ObjectType = 0

    def __init__(self, index, parameterName, objectType):
        self.index = index
        self.parameterName = parameterName
        self.objectType = objectType

    def __str__(self):
        return str(self.index)+': '+self.parameterName+' ObjectType: '+self.objectType

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
            if len(section) is 4:
                pn = eds.get(section, 'ParameterName')
                objtype = eds.get(section, 'ObjectType')
                hexIndex = int(section, 16)
                obj = DictObj(hexIndex, pn, objtype)
                dic.names[pn] = obj
                dic.ids[hexIndex] = obj
        return dic

    def __setitem__(self,key,value):
        if type(key) is str:
            self.names[key] = value
        else:
            self.ids[key] = value

    def __getitem__(self,key):
        if type(key) is str:
            return self.names[key]
        if type(key) is type(0x0):
            return self.ids[key]
        else:
            print('unkown key: '+key)


    def __iter__(self):
        for objitem in self.ids:
            yield objitem

    def __len__(self):
        return len(self.ids)

    def __str__(self):
        return '\n'.join([str(obj) for obj in self.ids.values()])
        # for key in self.ids:
        #     print(key+': ')

if __name__ == '__main__':
    print("initializing motorController Dictionary")
    test = ObjectDictionary.initialize('../edsfiles/MotorController.eds')
    print(str(test.ids[0x1018]))
