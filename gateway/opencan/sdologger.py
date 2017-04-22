from gateway.core.systemlogger import logger

class SDOLog(object):
    log = {
        0x6077:0x0, #Torque
        0x6076:0x0, #Peak Torque
        0x606B:0x0, #Velocity Demand
        0x606C:0x0, #Velocity
        0x6080:0x0, #Max motor speed
        0x6083:0x0, #Max accel rate
        0x608D:0x0, #Acceleration notation index
        0x608e:0x0 #Acceleration dimension index




    }

    def __init__(self, sdo):
        self.sdo = sdo
        ping()

    def log(data):
        logger.info(hex(data[x:x+2])+' ' for x in range(0, len(data), 2))
        ping(Index)

    def ping(index):
