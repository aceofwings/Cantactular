import struct
import time
class CanOutlet():
    """
    Base Outlet responsible for filtering and fowarding messages to the Engine

    Outlets are stream based objects thats sole purpose is interpret a message
    at its base most level. Of course outlets can deconstruct messages to any format
    but it should be left to the Core or Applications to further interpret the data

    """
    can_frame_fmt = "=IB3x8s"

    def init(self,engine,message_type=None):
        self.base = message_type
        self.__engine = engine

    def deconstruct_can_message(self,message):
        """
        Deconstruct the raw byte message to form a dictionary representation

        Override to customize the format and attributes of the message dictionary


        returns a dictionary representing the canmessage
        """
        canid, dlc, data = struct.unpack(self.can_frame_fmt,message)
        return {'message' : {'canid' : canid, 'dlc' : dlc, 'data' : data}, 'recieved' : time.time()
                    'type': self.base}

    def deconstruct_error_message(self,message):
        pass


    def validate(self,can_d):
        """
        Validate the deconstructed message. This can be implemented to limit
        the types of messages to be fowarded.

        Overide to add additional condition checking. Later black or white listing
        will be a feature to implement

        Due to the nature of the engine, filtering should be done by CanID,

        """
        return True

    def __validate_and_send(self,can_d):
        if self.validate(can_d):
            self.__engine.COREsend(can_d)

    def forward(self,message):
        """
        will deconstruct the message recieved from a canbus and determine
        whether for send the message to the engine for further processing.
        """
        can_d = self.deconstruct_can_message(message)
        self.__validate_and_send(can_d)

    def forward
