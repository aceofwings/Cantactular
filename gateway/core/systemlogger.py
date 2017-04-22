import logging
from logging.handlers import RotatingFileHandler
from gateway.utils.projectpaths import common
import os.path


logger = logging.getLogger('gateway')


class RunRotatingtHandler(RotatingFileHandler):

    extension = ".log"

    def __init__(self,filename, mode='a',encoding=None,delay=False, freshRun = False):
        if freshRun:
            filename = self.generateFileName(filename)
            print(filename)
        super().__init__(filename=filename)
    def rotation_filename(self,defaultName):
        super().rotation_filename(defaultName)

    def logfileExists(self,filename):
        return  os.path.exists(os.path.join(common.log, filename))

    def generateFileName(self,filename,number=0):
        basename = os.path.splitext(filename)[0]
        if self.logfileExists(basename + str(number) + self.extension):
            number += 1
            return self.generateFileName(basename, number)
            
        return basename + str(number) + self.extension
