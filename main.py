from sin_wawe import sin_wawe
import time

import dynamic_chart
from static_chart import figure_2






def main():

#------------------------------------------------1
    #figure_1() # realtime chart
#------------------------------------------------1

#------------------------------------------------2
#    chart_data = figure_1_1_init()
#    while True:
#        output = sin_wawe(10, 0, 10, time.process_time())  # amplitude, offset, period
#        chart_data = figure_1_1_input(chart_data, output)
#------------------------------------------------2

#------------------------------------------------3
    chart = dynamic_chart.chart()
    while True:
        output = sin_wawe(10, 0, 10, time.process_time())  # amplitude, offset, period
        chart.figure_get_input(output)
        chart.figure_draw()
#------------------------------------------------3

#------------------------------------------------4
    #figure_2() # static chart
#------------------------------------------------4








if __name__ == "__main__":
    main()