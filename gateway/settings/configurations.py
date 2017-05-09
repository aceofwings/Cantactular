from gateway.opencan.opencancontroller import CanOpenController
from gateway.evtcan.controller import EvtCanController


class Configuration(object):
    #define the interfaces and their base controller types
    interfaceNames = {'can0':EvtCanController, 'can1': CanOpenController}
    #silence any error on loading user customizable controllers

    maindbcFile = "INTEL_EVT_CAN.dbc"

    failureSilence = False
    #force start the interfaces at the earliest moment
    forceStartInterfaces = False

    freshLogFileOnRun = True
    messageFormat  = "motorola"
    #load devices prior to any custom state change
    imediateLoadDevice = ["BMS0", "BMS1", "BMS2", "BMS3", "BMS4", "BMS5", "BMS6"]

    #prints loading info
    verbosity = True
