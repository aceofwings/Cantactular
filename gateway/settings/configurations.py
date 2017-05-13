from gateway.opencan.opencancontroller import CanOpenController
from gateway.evtcan.controller import EvtCanController


class Configuration(object):
    #define the interfaces and their base controller types
    interfaceNames = {'vcan0':EvtCanController, 'vcan1': CanOpenController}
    #silence any error on loading user customizable controllers

    maindbcFile = "INTEL_EVT_CAN.dbc"

    failureSilence = False
    #force start the interfaces at the earliest moment
    forceStartInterfaces = False

    freshLogFileOnRun = True
    messageFormat  = "motorola"
    #load devices prior to any custom state change
    imediateLoadDevice = ["BMS0", "BMS1", "BMS2", "BMS3", "BMS4", "BMS5", "BMS6"]

    #devicename : eds file Pairings listed here
    can_devices = {"MotorController" : "MotorController.eds"}

    #prints loading info
    verbosity = True
