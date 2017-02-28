#!/usr/bin/python3
import os
import sys
RUN_FILE = 'gateway/launcher.py'
LAUNCHER_FILE = 'launcher.py'
CALL_PATH = os.path.abspath('.')
currentdir = CALL_PATH
STOP_PATH = os.path.join('','/')

def lookForLauncher(path):
    return os.path.isfile(path)
def unpackLauncher(path):
    return open(path, 'r').read()

while True:
    checkDir = os.path.join(os.path.abspath('.'), RUN_FILE)
    launcher = lookForLauncher(checkDir)
    if launcher:
        print("Attemping to launch app....")
        f = unpackLauncher(checkDir)
        exec(f)
        break
    elif currentdir == STOP_PATH:
        print("Fail to find launcher")
        break
        os.chdir('..')
        currentdir = os.path.abspath('.')





# while True:
#         checkDir = os.path.join(currentdir, RUN_FILE)
#         launcher = lookForLauncher(checkDir)
#         if launcher:
#             print(checkDir)
#             print("Attemping to launch app")
#             f = unpackLauncher(checkDir)
#             exec(f)
#             break
#         elif currentdir == STOP_PATH:
#             print("Fail to find launcher")
#             break
#         else:
#             currentdir = os.path.realpath(os.path.join(currentdir, '..'))
