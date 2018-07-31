from gateway.can.control.matcher import Matcher, CannotMatch, ALL
from gateway.can.controllers.base import OPENCAN

class OpenCanMatcher(Matcher):
    match_type = OPENCAN
    match = {"*":[]}

#Match dictionary format
#    index0 : {subindex0: [hanlders...], subindex1: [handlers...]},

    def __init__(self):
        super().__init__()

    def setup_quick_match(self):
        #build match dictionary
        #hanlder.match should be (index, subindex)
        for handler in self.handlers:
            if (handler.match[0] in self.match) and (type(handler.match[0]) is str):
                self.match[handler.match[0]].append(handler)#int ALL
            elif handler.match[0] in self.match:#index exists
                if handler.match[1] in self.match[handler.match[0]]:#subindex exists
                    self.match[handler.match[0]][handler.match[1]].append(handler)
                else:#index exists, subindex does not
                    self.match[handler.match[0]][handler.match[1]] = [handler]
            else:#index does not exist yet
                self.match[handler.match[0]] = {handler.match[1]: [handler]}

    def match_and_handle(self, message):
        for handle in self.match["*"]:
            handle(message)
        #
        # print("Matching message into...")
        # print(self.match)
        # print("Message attributes")
        # print(dir(message))
