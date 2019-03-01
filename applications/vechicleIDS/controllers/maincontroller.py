from gateway.can.controllers.base import BaseController
from gateway.core.service import Service
from gateway.core.service import Service
from threading import Thread
from collections import deque
from matplotlib import pyplot, animation
from lib import changepoint
import numpy as np
import time
pyplot.ion()
windowsize = 50

SUPPOSED_MESSAGE_FREQUENY = 50 #hz
THREAH_HOLD_LOW = 45 #hz
TREASH_HOLD_HIGH = 55 #hz

XMAX = 1000
class MainController(BaseController):

    allotment = [0] * 3000
    runningavg= [0] * int((XMAX/windowsize))
    runningvariance = [0] * int((XMAX/windowsize))
    runningavgx= [i for  i in range(0,XMAX,windowsize)]
    cps = [0] * 3000
    lastmessage = None
    running_avg = 0
    current = None
    last = None
    num_of_message = 0
    n = 0
    n2 = 0
    xyline = 0
    def __init__(self):
        print("intialize MainController")
        self.firstMessage = True
        self.secondMessage = True
        self.figure = pyplot.figure()
        self.graph = self.figure.add_subplot(111)
        self.plot , = self.graph.plot(self.allotment)
        self.runningplot , = self.graph.plot(self.runningavg)
        self.animation = animation.FuncAnimation(self.figure,self.update)
        pyplot.ylim(0,10)
        pyplot.xlim(0,200)
        pyplot.title('50 message windows', fontsize=18)
        pyplot.xlabel('Samples',fontsize=18)
        pyplot.ylabel('# of Messages', fontsize=18)
        #service = Service(target=evtcurses.startCurses,clean_up=self.end)
        # pyplot.show()


    @BaseController.handleEvt(0x81)
    def handleMessage(self,message):
        message.Cell_no0()
        if self.last is None:
            self.last = time.time()
        if self.current is None:
            self.current = time.time()

        self.num_of_message += 1
        if self.current - self.last > .05:
            self.last = self.current
            self.allotment[self.n] = self.num_of_message
            self.num_of_message = 0
            self.simple_move_average()
            self.n += 1

        self.current = time.time()

    def simple_move_average(self):
        if self.n % windowsize == 0:
            window =  self.allotment[(self.n - windowsize): self.n ]
            if len(window) != 0:

                self.runningavg[self.n2] =  sum(window) / len(window)
            #    self.runningvariance[self.n2] = sum([(xi - self.runningavg[self.n2]) ** 2 for xi in window]) / len(window)
                changepoints = changepoint.pelt(changepoint.normal_mean(window,2), len(window))
                if len(changepoints) > 1:
                    self.cps[self.n2] = self.runningavgx[self.n2]

            self.n2 += 1



    def update(self,void):
        self.plot.set_ydata(self.allotment)
        self.runningplot.set_ydata(self.runningavg)
        self.runningplot.set_xdata(self.runningavgx)
        self.graph.vlines(self.cps,0,20)

    # def running_avg_linear_weight(self):
    #     """take the arithmatic average """
    #     sum = 0
    #     for i in range(len(self.allotment)):
    #         sum += self.allotment[i]
    #     self.running_avg =  (sum / len(self.allotment))
    #     #print(self.running_avg)


    def end(self):
        print("ended")
