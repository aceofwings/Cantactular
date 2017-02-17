import collections, configparser
import os

class DictionaryObject(collections.Mapping):

    def __init__(self, index, subindex = None):
        self.index = index
        self.subindex = subindex
        self.attributeDictionary = {}
        self.subArray = []

    def __getitem__(self, key):
        if len(self.subArray) > 0: #check if has sub array
            if type(key) is int:    #checking by index
                return self.subArray[key]
            else:                   #checking by parameter name
                for sub in self.subArray:
                    if sub.parametername in key:
                        return sub
        else:
            return None

    def __getattr__(self, item):
        return self.attributeDictionary[item]

    def setAttribute(self, key, value):
        self.attributeDictionary[key] = value

    def __str__(self):
        if type(self.subindex) is type(None):
            string = '['+str(hex(self.index)) + ']'
        else:
            string = '['+str(hex(self.index)) +'sub'+str(self.subindex)+']'

        for attribute in self.attributeDictionary:
            string += '\n\t' + attribute +': '+ self.attributeDictionary[attribute]

        return string

    def __iter__(self):
        for objitem in self.varDic:#need to implement
            yield objitem

    def __len__(self):
        return len(self.varDic)#####need to fix to a length


class ObjectDictionary(collections.Mapping):
    edsFilePath = None

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
                hexIndex = int(section, 16)         # hex index represented as integer

                obj = DictionaryObject(hexIndex)

                for option in eds.options(section):
                    obj.setAttribute(option, eds.get(section, option))

                dic.names[pn] = obj
                dic.ids[hexIndex] = obj

            elif 'sub' in section:
                hexIndex = int(section.split('sub')[0], 16)
                subIndex = int(section.split('sub')[1], 16)

                obj = DictionaryObject(hexIndex, subIndex)

                for option in eds.options(section):
                    obj.setAttribute(option, eds.get(section, option))

                dic[hexIndex].subArray.append(obj)

        return dic

    def __setitem__(self,key,value):
        if type(key) is str:
            self.names[key] = value
        else:
            self.ids[key] = value

    def __getitem__(self,key):
        if type(key) is type(0x0):
            return self.ids[int(key)]
        if type(key) is str:
            return self.names[key]

    def __iter__(self):
        for objitem in self.ids:
            yield objitem

    def __len__(self):
        return len(self.ids)

    def __str__(self):
        return '\n'.join([str(obj) for obj in self.ids.values()])

if __name__ == '__main__':
    print("initializing motorController Dictionary")
    dictionary = ObjectDictionary.initialize('../edsfiles/MotorController.eds')

    print(dictionary[0x1018]['Serial number'])
