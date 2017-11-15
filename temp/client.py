import socket
import json


message = {'message' : {'name' : "DAN"}, 'type' : "MISC"}
new = {'message' : {'HEADER' : "NEW_CONNECTION", 'app_address': "Woot"}, 'type' : "ENGINE"}

sever_address = 'evt.gateway.core.sock'
client = socket.socket( socket.AF_UNIX, socket.SOCK_DGRAM )
client.connect(sever_address)
#while True:
client.send(json.dumps(message).encode())
client.send(json.dumps(new).encode())
