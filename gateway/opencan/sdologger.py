from gateway.core.systemlogger import logger
import time

class SDOLog(object):
    readlog = {
        0x6068:0x0, #Current
        0x60FF:0x0, #Target Speed
        0x2620:0x0, #Throttle value
        0x2220:0x0, #Throttle input voltage
        0x6077:0x0, #Torque
        0x2721:0x0, #Vehicle Speed
        0x606C:0x0, #Velocity
    }
    writelog = {
        0x2220:0x0 #Throttle input voltage
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
        pname = self.sdo.objectDictionary[index].parametername
        self.sdo.device.values[pname] = value

        self.sdo.read(self.readhandle, index, sub)

    def writehandle(self, message):
        #check if last was sucess!
        index = message.data[2]*256+message.data[1]
        #print(str(message.data)+"  index: "+str(index))
        write_times += 1
        self.sdo.write(self.writehandle, self.sdo.write_values[index], index, self.writelog[index])
