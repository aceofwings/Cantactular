
import logging
from logging.handlers import RotatingFileHandler
from gateway.utils.resourcelocator import ResourceLocator
import os

logger = logging.getLogger('gateway')

class RunRotatingtHandler(RotatingFileHandler):

    extension = ".log"

    def __init__(self,filename, mode='a',encoding=None,delay=False, freshRun = False):

        self.tempLocator = ResourceLocator.get_locator('temp')

        if freshRun:
            filename = self.generateFileName(filename)

        super().__init__(filename=filename)

    def rotation_filename(self,defaultName):
        super().rotation_filename(defaultName)

    def logfileExists(self,filename):
        return  os.path.exists(os.path.join(self.tempLocator.ROOT_PATH, filename))

    def generateFileName(self,filename,number=0):
        basename = os.path.splitext(filename)[0]
        if self.logfileExists(self.tempLocator.ROOT_PATH + basename + str(number) + self.extension):
            number += 1
            return self.generateFileName(basename, number)

        return self.tempLocator.ROOT_PATH  + basename + str(number) + self.extension


def loadLogger():
    logger = logging.getLogger('gateway')
    logger.setLevel(logging.DEBUG)
    infoformatter = logging.Formatter('%(levelname)s - %(message)s')
    fileformatter = logging.Formatter('%(message)s')
    fileHandler = RunRotatingtHandler("/track.log", freshRun = True)
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter(fileformatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(infoformatter)
    streamHandler.setLevel(logging.INFO)
    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)
