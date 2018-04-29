# Most Recent Gateway repository 

https://bitbucket.org/evt/gateway-applications

# Gateway

A Framework designed around implementing vehicle communications with ease.
Right now any message surround a dbc format can be encoded and decoded.
This framework concerns itself with being a passive listener.

Some current applications
 * Self-Driving
 * Self-Diagnostic
 * Logging
 * Playback



## Contributors and Team Members  
* Daniel Harrington
* Nick Amatruda

# Overview  
The Gateway is a raspherry PI accompanied by a PI-Can Cape. This device is mounted on the bike and connected to several other  devices such as the IMU and BMS through the protocol can-open.  

## Purpose
Implemented to follow can-open protocol and is able to operate effectivtly and effciently with many nodes on the network, retrieving various data measurements.

## How can *you* contribute?
Contributing is easy and must following our *guidelines*.

## Resources
* [CanOpen](https://en.wikipedia.org/wiki/CANopen)
* [DBC File Format](https://wiki.rit.edu/pages/viewpage.action?spaceKey=EVT&title=CAN+Database)

## install
```
python3 setup.py install
```
To setup the testing interface run
```
cansetup
```
