import collections

class ObjectDictionary(collections.Mapping):

    def __init__(self):
        self.names = {}
        self.ids = {}
    @classmethod
    def initialize(edsPath):
        pass

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
   test = ObjectDictionary()
