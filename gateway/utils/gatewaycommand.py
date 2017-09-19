class GatewayCommand(object):

    #commands alias
    alias = None

    def __init__(self,arguments):
        pass

    #should not overide
    def extendArgparse(argparser):
        pass

    #overide
    def arguments(self):
        pass

    #overide
    def run(self):
        pass
