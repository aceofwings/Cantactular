import socket
import json


message = {'message' : {'name' : "DAN"}, 'type' : "MISC"}
sever_address = 'evt.gateway.core.sock'
client = socket.socket( socket.AF_UNIX, socket.SOCK_DGRAM )
client.connect(sever_address)

client.send(json.dumps(message).encode())
