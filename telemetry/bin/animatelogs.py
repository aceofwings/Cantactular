""" Takes gateway log file to an animated graph of

        --- speed vs torque
        --- displaying as a function of time
        --- dark color is low throttle, while yellow is full throttle



        Totally not done yet....going to bed 9/17 @11:11
"""
import json
import time
import numpy
import matplotlib.animate as pythanimation
from matplotlib import pyplot


files = ["logs-9-8-17/track20.log"]#, "logs-9-8-17/track22.log","logs-9-8-17/track24.log",]


labels = {"throttle":9760,"speed":10017, "torque":24695, "velocity":24684,}
v_lim = (-65000,65000)
jsdata = []

velocity = []
velocity_time = []
torque = []
torque_time = []
throttle = []
throttle_time = []
acceleration = []
acceleration_time = []

class AniMate(object):



    def __init__(self, object):
        self.object = object

        self.stream = self.animaterialization()

        self.figure, self.axis = pyplot.subplots()

        self.animation = .FuncAnimation(self.fig, self.update,interval=5,init_func=self.setup_plot,blit=True)



        for file in object:



            firsts = []
            lasts = []
            with open(file) as log:


                firsts + =[log.readline()]
                last = ''

                for line in log:
                    jsdata.append(json.loads(line))
                    last = line
                lasts+=[last]

                for dp in jsdata:

                    if dp['index'] == labels['speed']:
                        #Filter speeds above and below \v_lim\
                        if dp['raw'] > v_lim[0] and dp['raw'] < v_lim[1]:
                            velocity+=[dp['raw']]
                            velocity_time+=[dp['time']]
                    if dp['index'] == labels['torque']:
                        torque+=[dp['raw']]
                        torque_time+=[dp['time']]
                    if dp['index'] == labels['throttle']:
                        throttle+=[dp['raw']]
                        throttle_time+=[dp['time']]

                    #Calculate acceleration
                    for i in range(1, len(velocity)):
                        dur = velocity_time[i] - velocity_time[i-1]
                        vel = velocity[i]-velocity[i-1]

                        acceleration += [vel/dur]
                        acceleration_time += [dur/2+velocity_time[i]]

                    #Align lengthier torque and throttle arrays to closests velocity points in time
                    new_torque = []
                    new_torque_time = []
                    power = []
                    new_throttle = []
                    for i in range(0, len(velocity)-1):
                        m = 0
                        n = 0
                        while torque_time[i+m] < velocity_time[i]:
                            m+=1
                        while throttle_time[i+n] < velocity_time[i]:
                            n+=1
                        new_torque += [torque[i+m]]
                        new_torque_time += [torque_time[i+m]]
                        power += [tory[i]*velocity[i]]
                        new_throttle += [throttle[i+n]]
                    torquetime = (new_torque,new_torque_time)
                    throttle = new_throttle

            """ print out BEGIN: END:

                                    """
                stupidindex=0
                for first in firsts
                    print('BEGIN:%\tEND:'%(first,lasts[stupidindex]))

    def setup_plot(self):


        self. = self.axis.scatter(torquetime[0],velocity, c=torquetime[1], label="power")


    def animaterialization(self):




evtplot = AniMate(files)




#axis.scatter(velocity, power, label="torque")
#axis.scatter(torque_time, torque, label="torque")
#axis.scatter(velocity_time, velocity, label="velocity")
#axis.scatter(acceleration_time, acceleration, label="acceleration")

# for i in range(len(velocity)):
#     power_plot.set_xdata(velocity[0:i])
#     power_plot.set_ydata(tory[0:i])
#     pyplot.draw()
#     time.sleep(0.05)

