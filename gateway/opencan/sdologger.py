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
        self.sdo.device.values = dict.fromkeys(self.readlog.keys())

        for key in self.readlog.keys():
            sdo.read(self.readhandle, key, self.readlog[key])
        for key in self.writelog.keys():
            sdo.write(self.writehandle, self.sdo.write_values[key], key, self.writelog[key])

    def readhandle(self, message):
        log = str(hex(message.canid))+' : '
        log += '['+str(hex(message.index))+'] '
        log += '['+str(hex(message.sub))+'] '
        log += '('+ str(hex(message.data[0])) +') '
        log += '='+ message.raw
        logger.debug(log)
        pname = self.sdo.objectDictionary[index].parametername
        self.sdo.device.values[index] = int(value, 16)

        self.sdo.read(self.readhandle, index, sub)

    def writehandle(self, message):
        #check if last was sucess!
        index = message.data[2]*256+message.data[1]
        #print(str(message.data)+"  index: "+str(index))
        self.sdo.write_times += 1
        self.sdo.write(self.writehandle, self.sdo.write_values[index], index, self.writelog[index])
