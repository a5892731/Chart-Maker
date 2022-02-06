'''

version 1.5.0

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



class Chartmaker:

    def __init__(self, chart_turn_on = True, plot_interval_ms = 50, chart_len_sec=5,
                 chart_title = '', x_name = '', y_name = ''):

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
        self.chart_turn_on = chart_turn_on
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
        plt.connect('close_event', self.on_click)

    def create_figure_from_lists(self, x_data, y_data):
        self.events() # check for events

        self.chart_time_ms = (time() - self.start_time) * 1000 # seconds
        if self.chart_time_ms > 2 * (self.chart_sample * self.plot_interval_ms): #interval time-out protection
            raise TimeoutError("to high interval frequency to plot chart: Plot interval: {} ms"
                               .format(self.plot_interval_ms, ))
        if self.chart_time_ms > (self.chart_sample * self.plot_interval_ms): #interval controll
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

    def on_click(self, event):
        if CloseEvent:
            self.chart_turn_on = False
            plt.close('all')
            print('chart close button turned on')


'''------------------------------------------------------------------------------------------------------------------'''

if __name__ == "__main__":

    '''start chart body'''
    plot_interval_ms = 100  # sample interval
    chart_len_sec = 10
    chart = Chartmaker(chart_turn_on = True, plot_interval_ms = plot_interval_ms, chart_len_sec=chart_len_sec,
                       chart_title = 'chart 1', x_name = 'x_name', y_name = 'y_name')  # create chart
    start_time = time()
    '''start chart body'''

    tests = ChartTests()  # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TESTING

    while chart.chart_turn_on:
        loop_start_time = time()  # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TESTING

        '''lop body'''
        current_time = time() - start_time
        y_data = sin_wawe(amplitude=10, offset=0, period=5, time= current_time)  # signal to plot

        chart.create_figure_from_lists(x_data = current_time, y_data = y_data)
        # give data to chart (y and x value)
        '''lop body'''

        program_execution_time = loop_start_time - time()  # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TESTING
        tests.print_test_data(chart, program_execution_time)  # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TESTING




