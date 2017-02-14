import os


#
# Paths to look for
#
common = {
'tests' : None,
'edsfiles' : None,
'rootpath' : None
}

class ProjectPath(object):
    def __init__(self,rootpath):
        self.paths = None
        self.buildProjectPaths(rootpath)
    """docstring for ProjectPaths."""
    def buildProjectPaths(self,rootpath):
        if common['rootpath'] is None:
            common['rootpath'] = rootpath
        directorys = os.listdir(rootpath)
        for directory in directorys:
            if  directory in common:
                path = os.path.join(rootpath,directory)
                common[directory] = path

    def __getattr__(self,key):
        return self.paths[key]
