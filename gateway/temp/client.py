import socket
import json
import os

message = {'message' : {'name' : "DAN"}, 'type' : "MISC"}

client_path = os.path.join(os.path.abspath("."),"cow")
sever_address = 'evt.gateway.core.sock'
client = socket.socket( socket.AF_UNIX, socket.SOCK_DGRAM )

if os.path.exists(client_path):
    os.unlink(client_path)

client.bind(client_path)

new = {'message' : {'HEADER' : "NEW_CONNECTION", 'app_address': client_path}, 'type' : "ENGINE"}

client.connect(sever_address)

client.sendto(json.dumps(message).encode(),sever_address)

client.send(json.dumps(new).encode())
client.send(json.dumps(message).encode())
# #while True:
#     print(client.recv(8048))
#     pass



client.close()
