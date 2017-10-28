import json
import struct
import time

"""
Takes Can Packet as list of 16 bytes
Also takes the endian of the data as a string ex."little","big"
bytes: list of integers, length should be 16
CAN Frame: CANID (4) , DataLen (1) , Padding (3) , Data (0 - 8)(Big Endian)
Returns JSON string
"""


def to_JSON( bytes, endian, network, type):
    messagedata = {'time': time.time()}
    messagedata['canid'] = -1
    messagedata['datalen'] = -1
    messagedata['data'] = -1
    messagedata['network'] = None
    messagedata['type'] = None
    if bytes is not None:
        messagedata['canid'] = int.from_bytes(bytes[0:4], byteorder=endian)
        messagedata['datalen'] = int(bytes[4])
        if messagedata['datalen'] == 0:
            messagedata['data'] = [0]
        else:
            messagedata['data'] = list(bytes[(16 - messagedata['datalen']):])
        messagedata['network'] = network
        messagedata['type'] = type
    return json.dumps(messagedata)


"""
Takes the formatted JSON string and convert it to CAN Frame (list of 16 bytes)
Also takes the endian of the data as a string ex."little","big"
Returns bytes list
"""


def from_JSON(jsonfile, endian):
    messagedata = json.loads(jsonfile)
    fstring = b'<IB3x8s' if endian == 'little' else b'>IB3x8s'
    can = struct.pack(fstring, messagedata['canid'], messagedata['datalen'], bytes(messagedata['data']))
    can = list(can)
    can[8:] = (bytes(messagedata['data']))
    for i in range(8, 16 - messagedata['datalen']):
        can.insert(i, 0)
    can = bytes(can)
    return (can, messagedata['network'], messagedata['type'])