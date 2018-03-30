"""
Core enbodies the commanality that is shared between services. Currently
there are two types of services. Application and Server.

Within Core are the methods to handle can messages
"""

from threading import Thread,Event

class Service(Thread):
    service = True
    running = Event()

    def __init__(self, *args, clean_up = None, **kwargs ):
        args = [self.running]
        kwargs['args'] = args
        super().__init__(**kwargs)
        if clean_up is not None:
            self.clean_up_r = clean_up


    def clean_up_r(self,running):
        pass

    def clean_up(self):
        self.running.set()
