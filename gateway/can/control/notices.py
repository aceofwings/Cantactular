import json

class Notice(object):
    """
    A Notice is similiar to a post, saying that the state has changed. Notices are non crtical state changes. If a crtical event occurs,
    an Error should be consider to be fowarded to the Engine to handle that event. Notices may follow after an error has been resolved or
    a state change occurs.
    """

    def __init__(self):
        self.type = "ENGINE"

    def TO_JSON(self):
        return json.dumps({'type' : self.type})


class RecoverySuccessfull(Notice):
    """
    If a sockettimeout occurs, during an engine's recovery attempt and is able to sucessfully restart its recievers,
    a RecoverySucessFull notice will be sent.
    """
    def __init__(self,socket):
        super().__init__()
        self.socket = socket
        self.msg = "An reciever is starting to see data"

class NewConnection(Notice):
    def __init__(self, address):
        super().__init__()
        self.header =  "NEWCONNECTION"
        self.addr = address

    def TO_JSON(self):
        return json.dumps({'type': self.type, 'header' : self.header,'addr' : self.addr})
