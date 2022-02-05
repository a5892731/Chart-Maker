'''
to do: improve turning off...
'''


from resources.create_data_x_y_list import ChartData
from test_files.sin_wawe import sin_wawe

from time import process_time, time
import matplotlib.pyplot as plt
import numpy as np



class Chartmaker:

    def __init__(self, y_data, x_data, plot_interval_ms = 50, chart_len_sec=5,
                 chart_title = 'chart 1', x_name = 'x_name', y_name = 'y_name'):

        plt.ion()

        '''chart variables'''
        self.plot_interval_ms = plot_interval_ms
        self.chart_len_sec = chart_len_sec
        self.chart_title = chart_title
        self.x_name = x_name
        self.y_name = y_name
        '''plot variables'''
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.x = np.array(x_data)
        self.y = np.array(y_data)
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

    def create_figure(self, x_data, y_data):
        self.plot_interval_ms = 50
        self.chart_len_sec = 5

        self.chart_refresh()

        self.ax.set_xlim(x_data[0], x_data[-1])
        self.x = np.array(x_data)
        self.y = np.array(y_data)
        self.y_axis, = self.ax.plot(self.x, self.y, 'r-')  # Returns a tuple of line objects, thus the comma
        #self.y_axis.set_ydata(y_data)

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()


'''------------------------------------------------------------------------------------------------------------------'''

if __name__ == "__main__":

    plot_interval_ms = 50
    chart_len_sec = 5

    data = ChartData(plot_interval_ms=plot_interval_ms, chart_len_sec=chart_len_sec)
    chart = Chartmaker(y_data = data.y, x_data = data.x,
                       plot_interval_ms = plot_interval_ms, chart_len_sec=chart_len_sec,
                       chart_title = 'chart 1', x_name = 'x_name', y_name = 'y_name')
    start_time = time()

    while True:
        loop_start_time = time()
        x_data = time() - start_time
        y_data = sin_wawe(amplitude=10, offset=0, period=5, time= x_data)  # function to plot
        data.update_data(y_data=y_data, x_data=x_data)

        chart.create_figure(x_data = data.x, y_data = data.y)


        program_execution_time = loop_start_time - time()
        print('program_execution_time: {}'.format(program_execution_time))

