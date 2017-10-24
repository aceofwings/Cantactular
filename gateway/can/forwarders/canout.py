import struct

"""
Reserved for custom CanMessages and events from additional sources other
then the can Interfaces
"""

class CanOutlet():
    can_frame_fmt = "=IB3x8s"
    """

    """
    def init(self,engine,message_type=None):
        self.base = message_type
        self.__engine = engine
    """
    returns a dictionary representing the basemost message type
    overide to add additional attributes to be sent to the engine
    """
    def deconstruct_can_message(self,message):
        canid, dlc, data = struct.unpack(self.can_frame_fmt,message)
        return {'message' : {'canid' : canid, 'dlc' : dlc, 'data' : data}}

    def validate(self,can_d):
        return True

    def __validate_and_send(self,can_d):
        if self.validate(can_d):
            self.__engine.COREsend(can_d)

    def forward(self,message):
        can_d = self.deconstruct_can_message(message)
        self.__validate_and_send(can_d)
