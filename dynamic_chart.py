# author: a5892731
# date: 04.02.2022
# last update: 09.03.2022
# version: 2.0.0
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
from resources.dynamic_chart_matplotlib3 import Chartmaker, ChartData

from time import time
from threading import Thread
'''------------------------------------------------------------------------------------------------------------------'''

if __name__ == "__main__":

    '''pre configuration'''
    chart_len_sec = 5.0  # seconds
    plot_refresh_time = 1.0  # seconds
    update_interval_data = 0.01  # update_interval_data [seconds]; 0 = MAX POSIBLE SPEED

    data = ChartData(chart_len_sec=chart_len_sec)
    chart = Chartmaker(chart_active=True,
                       chart_title='test chart', x_name='time [s]', y_name='amplitude [inc]')

    '''prepare data for x (time) axis'''
    start_time = time()

    while True:  # this will be a loop of your program

        if chart.chart_active:
            '''prepare data sample for x and y axis'''
            x_data = time() - start_time
            y_data = sin_wawe(amplitude=10, offset=0, period=5, time=x_data)  # function to plot

            '''create threads >>>'''
            threads = []
            '''create data array'''
            thread = Thread(target=data.update_data(y_data=y_data, x_data=x_data,
                                                    update_interval_s=update_interval_data))
            threads.append(thread)
            '''create chart'''
            thread = Thread(target=chart.create_figure(x=data.x_array, y=data.y_array,
                                                       plot_refresh_time=plot_refresh_time))
            threads.append(thread)
            '''start threads'''
            for thread in threads:
                thread.start()
            '''wait for all threads to end'''
            for thread in threads:
                thread.join()
            '''<<< create threads'''
        else:
            chart.close_figure() # this function will close all figures.

            break # this break is for closing main loop of this program.

