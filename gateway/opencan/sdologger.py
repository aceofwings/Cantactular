from gateway.core.systemlogger import logger
import time

class SDOLog(object):
    readlog = {
        0x6068:0x0, #Current
        0x60FF:0x0, #Target Speed
        0x2620:0x0, #Throttle value
        0x6077:0x0, #Torque
        0x6076:0x0, #Peak Torque
        0x2721:0x0, #Vehicle Speed
        0x606B:0x0, #Velocity Demand
        0x606C:0x0, #Velocity
        0x6080:0x0, #Max motor speed
        0x6083:0x0, #Max accel rate
        0x608D:0x0, #Acceleration notation index
        0x608e:0x0 #Acceleration dimension index
    }
    writelog = {
        #0x2220:0x00 #Throttle input voltage

        }

    def __init__(self, sdo):
        self.sdo = sdo
        for key in self.readlog.keys():
            sdo.read(self.readhandle, key, self.readlog[key])
        for key in self.writelog.keys():
            sdo.write(self.writehandle, self.sdo.write_values[key], key, self.writelog[key])

    def readhandle(self, message):
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
        print(self.sdo.objectDictionary[index][sub].parametername+" "+value)
        self.sdo.read(self.readhandle, index, sub)

    def writehandle(self, message):
        #check if last was sucess!
        index = message.data[2]*256+message.data[1]
        #print(str(message.data)+"  index: "+str(index))
        time.sleep(0.3)
        self.sdo.write(self.writehandle, self.sdo.write_values[index], index, self.writelog[index])
