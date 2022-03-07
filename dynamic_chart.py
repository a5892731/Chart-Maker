# author: a5892731
# date: 04.02.2022
# last update: 07.02.2022
# version: 1.5.1
#
# description:
# This is a program that create a dynamic chart
#
'''
Comments [ENG]:
-Depending on the device on which the program will work, the requirements will change for the maximum possible signal
sampling frequency on the graph. If the sampling interval (the plot_interval_ms variable) is too small for the computer
to realize it, an alarm will be reported:
TimeoutError ("to high interval frequency to plot chart on this device: Plot interval: {plot_interval_ms} ms"


Comments [PL]:
-W zależności od urządzenia na którym będzie pracować program, będą ulegać zmianie dotyczące wymagań na maksymalną
możliwą do wykonania częstotliwość próbkowania sygnału na wykresie. Jeśli interwał próbkowania
(zmienna plot_interval_ms) będzie zbyt mała by komputer mógł ją zrealizować, to zostanie zgłoszony alarm:
TimeoutError("to high interval frequency to plot chart on this device: Plot interval: {plot_interval_ms} ms"


'''


from test_files.sin_wawe import sin_wawe
from resources.dynamic_chart_matplotlib2 import Chartmaker

from time import time

'''------------------------------------------------------------------------------------------------------------------'''

if __name__ == "__main__":

    plot_interval_ms = 200  # sample interval
    chart_len_sec = 5

    chart = Chartmaker(chart_active = True, plot_interval_ms = plot_interval_ms, chart_len_sec=chart_len_sec,
                       chart_title = 'chart 1', x_name = 'x_name', y_name = 'y_name')  # create chart
    start_time = time()

    while chart.chart_active:
        current_time = time() - start_time
        y_data = sin_wawe(amplitude=10, offset=0, period=5, time= current_time)  # signal to plot

        chart.create_figure(x_data = current_time, y_data = y_data) # give data to chart (y and x value)


