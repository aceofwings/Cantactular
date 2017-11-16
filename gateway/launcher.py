<<<<<<< HEAD
#Use project paths as root path and configuration.
#Do not import this file directory

=======
"""
Launcher.py
Responsible for mapping out project resources and intializing any other
shared resources used between commands.

"""
>>>>>>> rev2devd
#Preconfiguration Code goes here
#Do not put code for specific applications here.
#Shared resource code would benefit if done in the launcher.
#
import os
<<<<<<< HEAD
from gateway.utils.projectpaths import ProjectPath
from gateway.settings.loader  import loadLogger

#setup the project path
ROOT_PATH = os.path.abspath('.')
ProjectPath(ROOT_PATH)
loadLogger()

#import commands
import gateway.core.engine
from . import commands
=======
import logging
from gateway.command import gatewayCommandLine
from gateway.utils.resourcelocator import ResourceLocator

ROOT_PATH = os.path.abspath('.')
ResourceLocator.ROOT_PATH = ROOT_PATH
gatewayCommandLine()
>>>>>>> rev2devd
