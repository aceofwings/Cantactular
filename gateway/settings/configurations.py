from gateway.opencan.opencancontroller import CanOpenController


class Configuration(object):
    #define the interfaces and their base controller types
    interfaceNames = {'vcan0' : CanOpenController}
    #silence any error on loading user customizable controllers
    failureSilence = True
    #force start the interfaces at the earliest moment
    forceStartInterfaces = False
    #load devices prior to any custom state change
    imediateLoadDeivce = "BMS"
