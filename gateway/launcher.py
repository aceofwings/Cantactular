"""
Launcher.py
Responsible for mapping out project resources and intializing any other
shared resources used between commands.

"""
#Preconfiguration Code goes here
#Do not put code for specific applications here.
#Shared resource code would benefit if done in the launcher.
#
import os
from gateway.command import gatewayCL
#from gateway.utils.projectpaths import ProjectPath
#from gateway.settings.loader  import loadLogger

#setup the project path
ROOT_PATH = os.path.abspath('.')
#ProjectPath(ROOT_PATH)
#loadLogger()
#import gateway.core.engine

#launch the gateway command line and parse command line args
gatewayCL()
