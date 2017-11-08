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
    pass

class InvalidMessageFormat(EngineError):
    pass

class CanSocketTimeout(EngineError):
    pass
