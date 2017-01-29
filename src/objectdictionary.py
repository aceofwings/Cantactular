 import collections, configparser

class DictObj():
    index = 0x0
    ParameterName = ''
    ObjectType = 0

    def __init__(self, index, parameterName, objectType):
        self.index = index
        self.ParameterName = parameterName
        self.ObjectType = objectType

class Record(DictObj):
    SubNumber = 0
    OBJECT = ''
    SECTION = ''
    CATEGORY = ''
    Subs = []

    def __init__(self, subnumber, obj, section, category):
        DictObj.__init__(self, index, parameterName, 9)
        self.SubNumber = subnumber
        self.OBJECT = obj
        self.SECTION = section
        self.CATEGORY = category

        # imcomplete/ not accurate 
        for sub in SubNumber:
            Subs += []




class Value(DictObj):
    DataType =0
    AccessType = ''
    LowLimit = 0
    HighLimit = 0 #might be hex value
    PDOMapping = 0
    DefaultValue = 0
    OBJECT_VERSION = 0 
    ACCESS_LEVEL = 0
    SCALING = 0
    EEPROM = ''

    def __init__(self, datatype, accesstype, lowlimit, highlimit, pdomapping, defaultvalue, object_verison, access_level, scaling, eeprom):
        self.DataType = datatype
        self.AccessType = accesstype
        self.LowLimit = lowlimit
        self.HighLimit = highlimit
        self.PDOMapping = pdomapping
        self.DefaultValue = defaultvalue
        self.OBJECT_VERSION = object_verison 
        self.ACCESS_LEVEL = access_level
        self.SCALING = scaling
        self.EEPROM = eeprom

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
        if type(key) is str:
            self.names[key] = value
        else:
            self.ids[key] = value

    def __getitem__(self,key):
        if type(key) is str:
            return self.names[key]
        else:
            return self.ids[key]


    def __iter__(self):
        for objitem in self.ids:
            yield objitem


    def __len__(self):
        return len(self.ids)



if __name__ == '__main__':

    cow = ObjectDictionary.initialize('..\edsfiles\MotorController.eds')
    feature-initialize-ObjectDictionary
