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
from gateway.utils.resourcelocator import ResourceLocator
from gateway.launchers.controlerize import load_controllers

ROOT_PATH = os.path.abspath('.')
ResourceLocator.ROOT_PATH = ROOT_PATH
if "__name__" == "gateway.templates.launcher":
    try:
        import controllers
        load_controllers(controllers)
    except ImportError:
        print("No Controllers Found")
