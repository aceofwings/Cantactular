#
#
#
#
#
#
#
#
#
#
#
#
class Listener:

    def __init__(self):
        self.listening = {}


    def notify(self,canmessage):
        print("Listener recv: "+canmessage)
