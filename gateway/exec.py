#!/usr/bin/python3
"""
exec.py

Helps find local project launcher. Changes current working directory until
launcher is found.

This allows us to call gateway locally anywhere in our project.  Changing
working directories to a known point in the project will allow for the an easier
way to map project assets.

If it successfully finds the launcher file, our working directory should now
be at the top level of this project, gateway-applications.

"""
import os
import sys

def main_func_gateway():
    RUN_FILE = os.path.join('gateway', 'launcher.py')
    LAUNCHER_FILE = 'launcher.py'
    CALL_PATH = os.path.abspath('.')
    currentdir = CALL_PATH
    STOP_PATH = os.path.join('','/')

    def lookForLauncher(path):
        return os.path.isfile(path)
    def unpackLauncher(path):
        return open(path, 'r').read()
    #Loop through until a launcher is found or until it has exhausted all parent directories('/')
    while True:
        checkDir = os.path.join(os.path.abspath('.'), RUN_FILE)
        launcher = lookForLauncher(checkDir)
        if launcher:
            f = unpackLauncher(checkDir)
            exec(f)
            break
        elif currentdir == STOP_PATH:
            print("Fail to find launcher")
            break
        os.chdir('..')
        currentdir = os.path.abspath('.')
