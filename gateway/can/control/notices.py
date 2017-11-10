

class Notice(object):
    pass


class RecoverySuccessfull(Notice):
    def __init__(self,socket):
        self.socket = socket
        self.msg = {'message' : {'notice' : "A socket is receiving traffice"} , 'type' : 'NOTICE'}
