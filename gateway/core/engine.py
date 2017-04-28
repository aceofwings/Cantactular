from gateway.settings.loader import loadDevices, loadInterfaces, _resources , startInterfaces, loadLogger
from gateway.core.systemlogger import logger

logger.info("Loading Device Configuration")
loadDevices()
logger.info("Device configurations Finished" )

logger.info("Configuring interface")
loadInterfaces()
logger.info("Configuring interfaces Finished")

logger.info("Attempting to spin up interfaces %s", _resources.busInterfaceNames)
startInterfaces()
logger.info("interfaces started")

deviceConstruct = _resources.deviceConstruct