# author: a5892731
# date: 04.02.2022
# last update: 06.02.2022
# version: 1.5.0
#
# description:
# This is a program that create a dynamic chart
#
'''

If you wont to know how to build signal, go to file test_files.static_signals

'''


from test_files.sin_wawe import sin_wawe
from resources.dynamic_chart_matplotlib2 import Chartmaker


from time import time

'''------------------------------------------------------------------------------------------------------------------'''

if __name__ == "__main__":

    plot_interval_ms = 100  # sample interval
    chart_len_sec = 5

    chart = Chartmaker(chart_turn_on = True, plot_interval_ms = plot_interval_ms, chart_len_sec=chart_len_sec,
                       chart_title = 'chart 1', x_name = 'x_name', y_name = 'y_name')  # create chart
    start_time = time()

    while chart.chart_turn_on:
        current_time = time() - start_time
        y_data = sin_wawe(amplitude=10, offset=0, period=5, time= current_time)  # signal to plot

        chart.create_figure_from_lists(x_data = current_time, y_data = y_data)
        # give data to chart (y and x value)


