"""
This file contains all things exception
"""
class EngineError(Exception):
    def finish():
        """
        if the error has been handled, a finisher will attempt to either check whether
        a correction has been made or ultimately change the state of an object.
        """
        pass
class NonExtistentType(EngineError):
    """
    Thrown when an incoming message has an unidentifiable type.
    """
    def __init__(self,msg):
        super().__init__()
        self.msg = msg

class InvalidMessageFormat(EngineError):
    """
    Thrown when an incoming message cannot be formated to the correct message object
    """
    pass

class RecoveryTimeout(EngineError):
    """
    Thrown when the engine is in recovery mode and the timeout expires
    without seeing any change in traffic
    """
    def __init__(self,socket):
        super().__init__()
        self.socket = socket
class CanSocketTimeout(EngineError):
    """
    Thrown when a cansocket timeouts out due to a lack of traffic
    """
    def __init__(self,socket):
        super().__init__()
        self.socket = socket

class NonExistentInterface(EngineError):

    def __init__(self,address):
        super().__init__()
        self.address = address
