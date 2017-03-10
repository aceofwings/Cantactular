from gateway.opencan.opencancontroller import CanOpenController


class Configuration(object):
    interfaceNames = {'vcan0' : CanOpenController}
    failureSilence = True
