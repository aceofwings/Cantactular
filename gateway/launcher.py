#Use project paths as root path and configuration.
#Do not import this file directory

#Preconfiguration Code goes here
#Do not put code for specific applications here.
#Shared resource code would benefit if done in the launcher.
#
import os
#from gateway.utils.projectpaths import ProjectPath
#from gateway.settings.loader  import loadLogger

#setup the project path
ROOT_PATH = os.path.abspath('.')
#ProjectPath(ROOT_PATH)
#loadLogger()
#import commands
#import gateway.core.engine
from . import command
