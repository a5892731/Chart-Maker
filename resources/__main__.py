from resources.sin_wawe import sin_wawe
from resources.dynamic_chart import Chart

from time import process_time



class Main():

    def __init__(self, chart_name="Chart 1", *args):

        self.chart_name = chart_name


    def call_dynamic_chart(self, *args):
        chart = Chart()
        chart.chart_title = self.chart_name
        #chart2 = dynamic_chart.chart()   # works very badly when calling two plots
        #chart2.chart_title = "2"

        while True:
            # sin_wawe(amplitude, offset, period, time)
            output1 = sin_wawe(10, 0, 5, process_time())  # works ok
            output2 = sin_wawe(10, 0, 1, process_time())  # bad refreshment # amplitude, offset, period
            output3 = 2 * process_time() + 5
            output4 = 3 * process_time() + 5

            chart.figure_get_input(args)
            chart.figure_draw()






# ------------------MAIN--------------------

if __name__ == "__main__":





    while True:
        data = sin_wawe(10, 0, 5, process_time())
        main = Main("Chart 1", data)