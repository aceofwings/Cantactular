#Author Daniel Harrington
#
#
#class Path
#An attribute dictionary that can be called to get path values
#
class Path(dict):
    def __getattr__(self,key):
        return self[key]
