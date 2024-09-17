""" from collections import deque
import time
import logging

import matplotlib.pyplot as plt
import numpy as np


def plot_main(proximity_sensor_front_queue: deque, proximity_sensor_btm_queue: deque, config):
    if config['plot_enabled']['proximity_sensor_front']:
        plt.ion()
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        plt.ylim([0,500])
        plt.xlim([0,30])

        data = np.random.randint(0,500,size=(50,))
        line, = ax.plot(data)

        ax.set_xlabel("Time (ms)")
        ax.set_ylabel("Data")
        ax.set_title("Title")
        ax.legend(['Data'],loc='upper right')

    
    while True:
        newdata=np.random.randint(0,500)
        data = np.append(data,newdata)
        
        if len(data)>100:
            data = data[-100:]

        line.set_ydata(data)
        line.set_xdata(np.arange(len(data)))
        plt.draw()
        plt.sleep(0.1) """