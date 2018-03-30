"""
Core enbodies the commanality that is shared between services. Currently
there are two types of services. Application and Server.

Within Core are the methods to handle can messages
"""

import json


class Provider(object):
    def COREreceive(self,message):
        can_d = json.loads(message.decode())
        self.controllers[can_d['type']].handle_message(can_d['message'])
        return can_d

    def get_type(self,message):
        return message['type']

    def COREsend(self,message):
        pass
    def COREerror(self,message):
        pass

    def CANsend(self,message):
        pass
    def CANreceivce(self,message):
        pass
