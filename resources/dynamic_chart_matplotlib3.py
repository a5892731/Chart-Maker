'''
version 1.5.2

to do in next version:
-add multi-charts
'''



from test_files.sin_wawe import sin_wawe
from test_files.chart_test import ChartTests


from time import process_time, time, sleep
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
        '''plot variables'''
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.chart_active = chart_active
        '''configuration'''
        self.chart_attributes()

    '''def __enter__(self):
        return self'''

    def chart_attributes(self):
        self.ax.set_title(self.chart_title)
        #self.ax.set_xlim(0, 10)
        #self.ax.set_ylim(-10, 10)
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
            self.chart_time = time()

            self.chart_refresh()  # refresh chart
            self.ax.set_xlim(min(x), max(x))
            self.y_axis, = self.ax.plot(x, y, 'r-')  # Returns a tuple of line objects, thus the comma
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()

        self.events()  # check for events
        self.lock.release()

    def on_click(self, event):
        if CloseEvent:
            self.chart_active = False
            plt.close()
            print('chart close button turned on')

    '''def __exit__(self, exc_type, exc_value, traceback):
        print('chart exit')'''


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
    plot_refresh_time = 2 # seconds
    update_interval_data = 0.01
    '''#update_interval_data [seconds] -> 
    minimal collecting data interval -> real value can by bigger. depends from CPU speed'''
    start_time = time()

    data = ChartData(chart_len_sec=chart_len_sec)

    chart = Chartmaker(chart_active = True,
                       chart_title = '', x_name = '', y_name = '')
    '''pre configuration'''

    while True:
        '''prepare data sample'''
        x_data = time() - start_time
        y_data = sin_wawe(amplitude=10, offset=0, period=5, time=x_data)  # function to plot

        '''create threads >>>'''
        threads = []

        '''create data array'''
        thread = Thread(target=data.update_data(y_data=y_data, x_data=x_data, update_interval_s=update_interval_data))
        check_chart_data()
        threads.append(thread)

        '''create chart'''
        if chart.chart_active:
            thread = Thread(target=chart.create_figure(x=data.x_array, y=data.y_array,
                                                       plot_refresh_time=plot_refresh_time))
            threads.append(thread)
        else:
            chart = Chartmaker(chart_active=False)

        '''start threads'''
        for thread in threads:
            thread.start()

        '''wait for all threads to end'''
        for thread in threads:
            thread.join()

        '''<<< create threads'''