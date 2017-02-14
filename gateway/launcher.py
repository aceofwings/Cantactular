#Use project paths as root path and configuration.
#Do not import this file directory

#Preconfiguration Code goes here
import os
from gateway.utils.projectpaths import ProjectPath
#setup the project path
ROOT_PATH = os.path.abspath('.')
ProjectPath(ROOT_PATH)
#import commands
from . import commands
