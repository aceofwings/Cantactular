"""
CAN Engine|
-----------

Daemon responsible for polling CAN Buses for incoming messages
and relaying to Core.

Nicholas and Federico
Amatruda and Rueda

"""

default_addresses = ['evt.gateway.core.sock', 'canOPEN', 'canEVT']
sockets = []

#Incoming messages to the Gateway
incomin_buffer = []
#Outgoing messages to CAN BUS
outgoing_buffer = []


"""
Takes Can Packet as list of 16 bytes
bytes: list of integers, length should be 16
CAN Frame: CANID (4) , DataLen (1) , Padding (3) , Data (0 - 8)(Big Endian)
Returns JSON string
"""
def to_JSON(bytes):
    pass

"""
Takes the formatted JSON string and convert it to CAN Frame (list of 16 bytes)
Returns bytes list
"""
def from_JSON(json):
    pass


"""
Creates and binds the sockets of the CAN engine to the default_addresses list.
Returns with GLOBAL list of socket objects instantiated
"""
def bindsockets():
    pass

"""
Daemon reads the CAN Bus specified by socket connection input
Messages recieved are converted to JSON and placed into incoming_buffer
"""
def CANread(sock):
    pass

"""
Daemon takes messages from the outgoing_buffer
JSON string is converted to bytes and sent across CAN socket
"""
def CANsend(sock):
    pass


"""
Daemon sends messages from incoming_buffer to core
"""
def COREsend(sock):
    pass

"""
Daemon polls the core socket for messages in JSON
Places core messages in outgoing_buffer if message type is CAN
Handles other events as necessary
"""
def COREreceive(sock):
    pass
