

"""
Reserved for custom CanMessages and events from additional sources other
then the can Interfaces
"""
class CanOutlet():
    """

    """
    def init(self,message_type):
        self.__base = message_type
    """
    returns a dictionary representing the basemost message type
    """
    def forwarder(message):
        return {'protocol' : self.__base}
