from sin_wawe import sin_wawe
import time

import dynamic_chart
import dynamic_chart2
from static_chart import figure_2


def main():

    def call_dynamic_chart():
        chart = dynamic_chart.Chart()
        chart.chart_title = "1"
        #chart2 = dynamic_chart.chart()   # works very badly when calling two plots
        #chart2.chart_title = "2"

        while True:
            # sin_wawe(amplitude, offset, period, time)
            output1 = sin_wawe(10, 0, 10, time.process_time())  # works ok
            output2 = sin_wawe(10, 0, 1, time.process_time())  # bad refreshment # amplitude, offset, period
            output3 = 2 * time.process_time() + 5
            output4 = 3 * time.process_time() + 5

            chart.figure_get_input(output3)
            chart.figure_draw()

            #chart2.figure_get_input(output4)
            #chart2.figure_draw()

    def call_static_chart():
        figure_2()  # static chart


    def call_dynamic_chart2():
        app = dynamic_chart2.QApplication(dynamic_chart2.sys.argv)
        dynamic_chart2.QApplication.setStyle(dynamic_chart2.QStyleFactory.create('Plastique'))
        myGUI = dynamic_chart2.CustomMainWindow()
        dynamic_chart2.sys.exit(app.exec_())

# ------------------MAIN--------------------


    call_dynamic_chart()

    #call_dynamic_chart2()

    #call_static_chart()






if __name__ == "__main__":
    main()