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
from gateway.command import gatewayCommandLine
ROOT_PATH = os.path.abspath('.')
gatewayCommandLine()
