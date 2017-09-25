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
import logging
from gateway.command import gatewayCommandLine
from gateway.utils.resourcelocator import ResourceLocator

ROOT_PATH = os.path.abspath('.')
ResourceLocator(ROOT_PATH).fetch_file("Hello.py")

gatewayCommandLine()
