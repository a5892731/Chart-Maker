'''
version 3.5.0

to do in next version:
-add multi-charts
'''

from test_files.sin_wawe import sin_wawe

from time import time, sleep
from matplotlib.backend_bases import CloseEvent
import matplotlib.pyplot as plt
import numpy as np
from threading import Thread, Lock


class ChartData:
    def __init__(self, chart_len_sec = 10, start_time = 0):
        self.lock = Lock()
        '''chart variables'''
        self.class_time = time()
        self.chart_len_sec = chart_len_sec
        self.statistic_data_interval = 0
        self.sample = 1
        '''empty x and y data lists'''
        self.x = [start_time]  #chart len in x axis
        self.y = [0]  # fill the graph with zeros at startup
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

class Chartmaker:  # use for 1 chart in window
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

    def create_chart_window(self):
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

    def events(self):
        '''chart window events'''
        '''x-button click in right corner of the chart event'''
        plt.connect('close_event', self.on_click)

    def on_click(self, event):
        if CloseEvent:
            self.chart_active = False
            print('chart close button turned on')

    def close_figure(self):
        #plt.close(fig='all')
        plt.close(fig='all')
        print('figure is closed')

'''------------------------------------------------------------------------------------------------------------------'''

class Chartsmaker(Chartmaker):   # use for more than 1 chart in window

    def initiation_of_chart_window(self, number_of_charts):
        '''TO DO'''
        '''chose one or more charts to plot in window'''
        None

    def create_charts_window(self, number_of_charts):
        self.axs = list() # list of axis
        self.number_of_charts = number_of_charts
        self.fig, self.axs = plt.subplots(self.number_of_charts, 1)

    def charts_attributes(self):
        for chart in range(self.number_of_charts):
            self.axs[chart].grid(True)

    def charts_refresh(self):
        for axis in range(len(self.axs)):
            self.axs[axis].clear()

    def create_figures(self, lists_of_x_data, lists_of_y_data, plot_refresh_time):
        self.lock.acquire()

        self.time_to_refresh = plot_refresh_time - (time() - self.chart_time)
        if self.time_to_refresh < 0:
            self.charts_refresh()
            for chart in range(len(lists_of_x_data)):
                self.axs[chart].plot(lists_of_x_data[chart], lists_of_y_data[chart])

            self.charts_attributes()

            self.fig.canvas.draw()
            self.fig.canvas.flush_events()

        self.events()  # check for events
        self.lock.release()
'''------------------------------------------------------------------------------------------------------------------'''

if __name__ == "__main__":

    def check_chart_data():
        #print(data.y_array)
        #print(data.x_array)
        print('current time {}'.format(x_data))
        print("first x element = {}".format(data.x[0]))
        print("last x element = {}".format(data.x[-1]))
        print("difference between first and last x element = {}".format(data.x[-1] - data.x[0]))
        print("statistic_data_interval = {}".format(data.statistic_data_interval))
        print("x data len = {}".format(len(data.x)))
        print("y data len = {}".format(len(data.y)))
        print()


    '''pre configuration'''
    chart_len_sec = 5 # seconds
    plot_refresh_time = 1 # seconds
    update_interval_data = 0.01 #update_interval_data [seconds]; 0 = MAX POSIBLE SPEED

    start_time = time()

    data = ChartData(chart_len_sec=chart_len_sec)
    data2 = ChartData(chart_len_sec=chart_len_sec)

    chart = Chartsmaker(chart_active = True,
                       chart_title = 'test chart', x_name = 'time [s]', y_name = 'amplitude [inc]')

    #chart.create_chart_window()
    chart.create_charts_window(number_of_charts=2)
    '''pre configuration'''

    while True:# this will be a loop of your program

        if chart.chart_active:
            '''prepare data sample'''
            x_data = time() - start_time
            y_data = sin_wawe(amplitude=10, offset=0, period=5, time=x_data)  # function to plot
            y_data2 = sin_wawe(amplitude=10, offset=0, period=2, time=x_data)  # function to plot


            '''create threads >>>'''
            threads = []
            '''create data array'''
            thread = Thread(target=data.update_data(y_data=y_data, x_data=x_data,
                                                    update_interval_s=update_interval_data))
            threads.append(thread)

            thread = Thread(target=data2.update_data(y_data=y_data2, x_data=x_data,
                                                    update_interval_s=update_interval_data))
            threads.append(thread)

            '''create chart'''

            thread = Thread(target=chart.create_figures(lists_of_x_data=[data.x_array, data2.x_array],
                                                        lists_of_y_data=[data.y_array, data2.y_array],
                                                        plot_refresh_time=update_interval_data))
            threads.append(thread)
            '''start threads'''
            for thread in threads:
                thread.start()
            '''wait for all threads to end'''
            for thread in threads:
                thread.join()
            '''<<< create threads'''

        else:
            chart.close_figure()
            print("end for 5")
            sleep(1)
            print("end for 4")
            sleep(1)
            print("end for 3")
            sleep(1)
            print("end for 2")
            sleep(1)
            print("end for 1")
            sleep(1)
            print("end for 0")

            break

