# author: a5892731
# date: 04.02.2022
# last update: 04.02.2022
# version: 1.3.0
#
# description:
# This program that creates a dynamic charts
#
'''

If you wont to know how to build signal, go to file test_files.static_signals

'''


from test_files.sin_wawe import sin_wawe
from resources.dynamic_chart_matplotlib import Chart

from time import process_time


if __name__ == "__main__":

    chart = Chart()
    chart.chart_attributes(chart_title = 'real time chart', y_axis_name = 'amplitude [inc]', x_axis_name = 'time [s]')

    while True:

        data = sin_wawe(amplitude = 10, offset = 0, period=5, time=process_time())
        chart.figure_get_input(y_axis = data, x_axis = process_time())
        chart.figure_draw(chart_len = 10)


