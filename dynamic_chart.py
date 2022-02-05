# author: a5892731
# date: 04.02.2022
# last update: 05.02.2022
# version: 1.4.0
#
# description:
# This program that creates a dynamic charts
#
'''

If you wont to know how to build signal, go to file test_files.static_signals

'''


from test_files.sin_wawe import sin_wawe
from resources.dynamic_chart_matplotlib2 import Chartmaker
from resources.create_data_x_y_list import ChartData

from time import time

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

