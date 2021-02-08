from sin_wawe import sin_wawe
import time
import matplotlib.pyplot as plt
from chart_type_1 import figure_1
from chart_type_1_1 import figure_1_1, figure_1_1_init, figure_1_1_input
import chart_type_1_2
from chart_type_2 import figure_2






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
    chart = chart_type_1_2.chart()
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