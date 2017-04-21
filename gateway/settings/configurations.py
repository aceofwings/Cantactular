from gateway.opencan.opencancontroller import CanOpenController
from gateway.evtcan.controller import EvtCanController


class Configuration(object):
    #define the interfaces and their base controller types
    interfaceNames = {'vcan0' : EvtCanController}
    #silence any error on loading user customizable controllers

    maindbcFile = "INTEL_EVT_CAN.dbc"

    failureSilence = True
    #force start the interfaces at the earliest moment
    forceStartInterfaces = False

    messageFormat  = "motorola"
    #load devices prior to any custom state change
    imediateLoadDeivce = ["BMS0"]

    #prints loading info
    verbosity = True
