from gateway.utils.projectpaths import ProjectPath
from gateway.opencan.opencancontroller import OpenCanController
from gateway.opencan.opencandevice import

class Gateway:
    def __init__():
        # find files to initilize controllers
        edsfile = 'mc.eds'
        evtfile = 'evt.dbc'

        openCanController = OpenCanController()
        openCanController.createInterface('can0')

        mcdevice = MotorControllerDevice(1, openCanController)

