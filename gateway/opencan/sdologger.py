from gateway.core.systemlogger import logger

class SDOLog(object):
    loglist = {
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
        for key in self.loglist.keys():
            sdo.read(self.handle, key, self.loglist[key])

    def handle(self, message):
        log = 'ID['+str(hex(message.canid))+'] '
        index = message.data[2]*256+message.data[1]
        log += 'index['+str(hex(index))+'] '
        sub = message.data[3]
        log += 'sub['+str(hex(sub))+'] '
        log += 'cb['+ str(hex(message.data[0])) +'] '
        value = 0x0
        for x in range(4, 8):
            log += str(hex(message.data[x]))[2:4]+" "
            value += message.data[x]
        log += '='+str(value)

        logger.debug(log)
        print(log)

        self.sdo.read(self.handle, index, sub)
