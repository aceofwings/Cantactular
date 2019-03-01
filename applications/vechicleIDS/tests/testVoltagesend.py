import os
import socket
import random
from time import sleep


import argparse

args = argparse.ArgumentParser()
args.add_argument("-period", "-t", default=.1, type=float)
arguments = args.parse_args()

test_socket = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
test_socket.bind(('vcan0',))

count = 0x80
#Calculate random data to mock CAN socket output
while(True):
    datalength =  random.randint(0, 8)
    can = list(count.to_bytes(4, byteorder='little'))
    can += [datalength]
    can += [0,0,0]
    for x in range(0, 8-datalength):
        can += [0x01,0x00,0x01]
    for y in range(0, datalength):
        can += [0X02]
    try:
        test_socket.send(bytearray(can))
        sleep(arguments.period)
    except OSError as e:
        pass
