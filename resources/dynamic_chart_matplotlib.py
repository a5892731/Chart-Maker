'''
version 2.0.0
and
version 3.0.0 - Doublee
'''

from time import time, sleep
from matplotlib.backend_bases import CloseEvent
import matplotlib.pyplot as plt
import numpy as np
from threading import Thread, Lock


class ChartData:
    def __init__(self, chart_len_sec = 10, start_time = 0, first_y=0):
        self.lock = Lock()
        '''chart variables'''
        self.class_time = time()
        self.chart_len_sec = chart_len_sec
        self.statistic_data_interval = 0
        self.sample = 1
        '''empty x and y data lists'''
        self.x = [start_time]  #chart len in x axis
        self.y = [first_y]  # fill the graph with zeros at startup
        self.x_array = np.array(self.x)
        self.y_array = np.array(self.y)
        self.create_array()

    def create_array(self):
        self.x_array = np.array(self.x)
        self.y_array = np.array(self.y)

    def update_data(self, y_data, x_data, update_interval_s = 0.1):
        '''add data to end of the datalists and remove its first element'''
        self.lock.acquire()
        self.time_to_refresh = update_interval_s - (time() - self.class_time)
        if self.time_to_refresh < 0:
            self.class_time = time()

            self.x.append(x_data)  # Add a new value 1 higher than the last.
            self.y.append(y_data)  # Add a new random value.

            for list_element in range(len(self.x)):
                if self.x[list_element] < self.x[-1] - self.chart_len_sec:
                    self.x = self.x[1:]  # Remove the first y element.
                    self.y = self.y[1:]  # Remove the first x element
                else:
                    break
            self.statistic_data_interval = self.x[-1] - self.x[-2]
            self.create_array()
        self.lock.release()
'''------------------------------------------------------------------------------------------------------------------'''

class Chartmaker:
    def __init__(self, chart_active = True,
                 chart_title = '', x_name = '', y_name = ''):
        self.lock = Lock()
        plt.ion()
        '''chart variables'''
        self.chart_time = time()
        self.time_to_refresh = 0
        self.chart_title = chart_title
        self.x_name = x_name
        self.y_name = y_name
        self.chart_active = chart_active
        '''pyplot variables'''
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)

    def chart_attributes(self):
        self.ax.set_title(self.chart_title)
        self.ax.set_xlabel(self.x_name)
        self.ax.set_ylabel(self.y_name)
        self.ax.grid(True)

    def chart_refresh(self):
        self.ax.clear()
        self.chart_attributes()

    def events(self):
        '''chart window events'''
        '''x-button click in right corner of the chart event'''
        plt.connect('close_event', self.on_click)

    def create_figure(self, x, y, plot_refresh_time):
        self.lock.acquire()

        self.time_to_refresh = plot_refresh_time - (time() - self.chart_time)
        if self.time_to_refresh < 0:
            self.chart_refresh()  # refresh chart
            self.chart_time = time()
            self.ax.set_xlim(min(x)-0.01, max(x)+0.01)
            self.y_axis, = self.ax.plot(x, y, 'r-')  # Returns a tuple of line objects, thus the comma
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()

        self.events()  # check for events
        self.lock.release()

    def on_click(self, event):
        if CloseEvent:
            self.chart_active = False
            print('chart close button turned on')

    def close_figure(self):
        plt.close(fig='all')
        print('figure is closed')
'''------------------------------------------------------------------------------------------------------------------'''

class DoubleChartmaker:
    def __init__(self, chart_active = True,
                 chart_title = '', x_name = ['', ''], y_name = ['', '']):
        self.lock = Lock()
        plt.ion()
        '''chart variables'''
        self.chart_time = time()
        self.time_to_refresh = 0
        self.chart_title = chart_title
        self.x_name = x_name
        self.y_name = y_name

        self.chart_active = chart_active
        '''pyplot variables'''
        self.fig, self.axis = plt.subplots(nrows=2)

        self.create_chart = True
        # because you can have more than 1 chart in this program



    def chart_attributes(self):
        #self.axs[0].set_title(self.chart_title)
        self.axis[0].set_xlabel(self.x_name[0])
        self.axis[0].set_ylabel(self.y_name[0])
        self.axis[0].grid(True)

        self.axis[1].set_xlabel(self.x_name[1])
        self.axis[1].set_ylabel(self.y_name[1])
        self.axis[1].grid(True)


    def chart_refresh(self):
        #self.axs.clear()
        self.chart_attributes()

    def events(self):
        '''chart window events'''
        '''x-button click in right corner of the chart event'''
        plt.connect('close_event', self.on_click)

    def create_figure(self, x, y, plot_refresh_time):
        self.lock.acquire()

        self.time_to_refresh = plot_refresh_time - (time() - self.chart_time)
        if self.time_to_refresh < 0:
            self.chart_refresh()  # refresh chart
            self.chart_time = time()
            self.axis[0].set_xlim(min(x[0])-0.01, max(x[0])+0.01)
            self.axis[1].set_xlim(min(x[1])-0.01, max(x[1])+0.01)

            self.y_upper_axis = self.axis[0].plot(x[0], y[0], 'r-')  # Returns a tuple of line objects, thus the comma
            self.y_bottom_axis = self.axis[1].plot(x[1], y[1], 'r-')  # Returns a tuple of line objects, thus the comma

            self.fig.canvas.draw()
            self.fig.canvas.flush_events()

            #self.fig.tight_layout()
            #plt.show()



        self.events()  # check for events
        self.lock.release()

    def on_click(self, event):
        if CloseEvent:
            self.chart_active = False
            print('chart close button turned on')

    def close_figure(self):
        plt.close(fig='all')
        print('figure is closed')