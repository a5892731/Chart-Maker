'''
version 1.5.2

to do in next version:
-add multi-charts
'''


from resources.create_data_x_y_list import ChartData
from test_files.sin_wawe import sin_wawe
from test_files.chart_test import ChartTests


from time import process_time, time
from matplotlib.backend_bases import CloseEvent
import matplotlib.pyplot as plt
import numpy as np
from threading import Thread, Lock


class Chartmaker:

    def __init__(self, chart_active = True, plot_interval_ms = 200, chart_len_sec=5,
                 chart_title = '', x_name = '', y_name = ''):
        self.lock = Lock()
        plt.ion()
        '''chart variables'''
        self.plot_interval_ms = plot_interval_ms # interval of getting samples for chart
        self.chart_len_sec = chart_len_sec - 1 # chart len in seconds -> -1 because it is counting from 0
        self.chart_title = chart_title
        self.start_time = time() # chart start time
        self.chart_sample = 1  # number of collected samples
        self.x_name = x_name
        self.y_name = y_name
        '''plot variables'''
        #self.fig, self.ax = plt.subplots()
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.chart_active = chart_active
        '''axis data'''
        self.data = ChartData(plot_interval_ms=plot_interval_ms,
                              chart_len_sec=chart_len_sec)  # x, y lists (with zeros) creator for chart turning on
        self.x = np.array(self.data.x) # array of x data to plot on start
        self.y = np.array(self.data.y) # array of y data to plot on start
        '''configuration'''
        self.chart_attributes()

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

    def create_figure(self, x_data, y_data):


        self.chart_time_ms = (time() - self.start_time) * 1000 # seconds
        if self.chart_time_ms > 2 * (self.chart_sample * self.plot_interval_ms): #interval time-out protection
            raise TimeoutError("to high interval frequency to plot chart on this device: Plot interval: {} ms"
                               .format(self.plot_interval_ms, ))



        if self.chart_time_ms > (self.chart_sample * self.plot_interval_ms): #interval controll

            self.lock.acquire()

            self.chart_sample += 1
            self.data.update_data(y_data=y_data, x_data=x_data)  # update x, y data lists
            self.chart_refresh() # refresh chart
            self.ax.set_xlim(self.data.x[0], self.data.x[-1])
            self.x = np.array(self.data.x) # create array from list
            self.y = np.array(self.data.y) # create array from list
            self.y_axis, = self.ax.plot(self.x, self.y, 'r-')  # Returns a tuple of line objects, thus the comma
            #self.y_axis.set_ydata(y_data)
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()

            self.lock.release()

        self.events()  # check for events


    def on_click(self, event):
        if CloseEvent:
            self.chart_active = False
            plt.close()
            print('chart close button turned on')


'''------------------------------------------------------------------------------------------------------------------'''

if __name__ == "__main__":

    '''start chart body'''
    plot_interval_ms = 1000  # sample interval
    interval_list = [600 for _ in range(25)]


    chart_len_sec = 10
    chart = Chartmaker(chart_active = True, plot_interval_ms = plot_interval_ms, chart_len_sec=chart_len_sec,
                       chart_title = 'chart 1', x_name = 'x_name', y_name = 'y_name')  # create chart

    chart2 = Chartmaker(chart_active = True, plot_interval_ms = plot_interval_ms, chart_len_sec=chart_len_sec,
                        chart_title = 'chart 2', x_name = 'x_name', y_name = 'y_name')  # create chart

    chart3 = Chartmaker(chart_active = True, plot_interval_ms = plot_interval_ms, chart_len_sec=chart_len_sec,
                        chart_title = 'chart 3', x_name = 'x_name', y_name = 'y_name')  # create chart


    start_time = time()

    '''start chart body'''

    tests = ChartTests()  # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TESTING

    while chart.chart_active:
        loop_start_time = time()  # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TESTING
        threads = []
        '''create threads'''


        '''lop body>'''
        current_time = time() - start_time
        y_data = sin_wawe(amplitude=10, offset=0, period=5, time= current_time)  # signal to plot
        y_data2 = sin_wawe(amplitude=5, offset=0, period=10, time= current_time)  # signal to plot

        '''create threads >>>'''
        thread = Thread(target=chart.create_figure(x_data = current_time, y_data = y_data))
        threads.append(thread)

        thread = Thread(target=chart2.create_figure(x_data = current_time, y_data = y_data2))
        threads.append(thread)

        thread = Thread(target=chart3.create_figure(x_data = current_time, y_data = y_data2))
        threads.append(thread)

        '''start threads'''
        for thread in threads:
            thread.start()

        '''wait for all threads to end'''
        for thread in threads:
            thread.join()

        '''<<< create threads'''


        #chart.create_figure(x_data = current_time, y_data = y_data) # give data to chart (y and x value)
        #chart2.create_figure(x_data = current_time, y_data = y_data2) # give data to chart (y and x value)
        '''lop body<'''



        program_execution_time = loop_start_time - time()  # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TESTING
        tests.print_test_data(chart, program_execution_time)  # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TESTING

        if program_execution_time < -0.1:
            interval_list.append(int(-program_execution_time*1000))
            interval_list.pop(0)
            new_interval = 0
            for inter in interval_list:
                new_interval += inter



            new_interval = int(new_interval / (len(interval_list) + 1) + 50)

            print('new interval: {} ms'.format(new_interval))

            chart.plot_interval_ms = new_interval
            chart2.plot_interval_ms = new_interval