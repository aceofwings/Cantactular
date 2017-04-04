import os
from gateway.utils.path import Path

#Author: Daniel Harrington
#Paths to look for in project
#

common = Path(
tests=None,
edsfiles=None,
rootpath=None
)

class ProjectPath(object):

    def __init__(self,rootpath=None):
        if rootpath is not None:
            self.__buildProjectPaths(rootpath)
    """docstring for ProjectPaths."""
    def __buildProjectPaths(self,rootpath):
        if common['rootpath'] is None:
            common['rootpath'] = rootpath
        directorys = os.listdir(rootpath)
        for directory in directorys:
            if  directory in common:
                path = os.path.join(rootpath,directory)
                common[directory] = path

    """
    if the resource is not properly loaded, it will just returned the fileName
    or path specified
    """
    @classmethod
    def edsfile(self, fileName):
        if common.edsfiles is not None:
            return os.path.join(common.edsfiles, fileName)
        else:
            return fileName
