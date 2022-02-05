'''
real time chart:

comments:
The chart is not suitable for collecting large amounts of data.

TO DO:
-Requires that the chart data cache be cleared over time. The reason is the systematic slowing down of the program.
-Need correction in chart closing/terminating
https://stackoverflow.com/questions/45135150/how-to-disable-the-close-button-in-matplotlib

'''
from test_files.sin_wawe import sin_wawe
from time import process_time


import matplotlib.pyplot as plt

class Chart():
    version = "1.3.0"

    def __init__(self):
        x = [None, None]
        y = [None, None]
        fig = plt.figure()
        ax = fig.add_subplot(111)
        self.chart_data = {"figure": fig, "axis": ax, "x-axis": x, "y-axis": y, "time": 0}

    def chart_attributes(self, chart_title = '', y_axis_name = '', x_axis_name = ''):
        self.chart_data["figure"].canvas.set_window_title(chart_title)
        plt.title(label=chart_title, fontsize=15, color="black")
        self.chart_data["axis"].set_xlabel(x_axis_name)
        self.chart_data["axis"].set_ylabel(y_axis_name)
        self.chart_data["axis"].grid(True)

    def figure_get_input(self, y_axis, x_axis, data_list_bufor_len = 2):
        self.chart_data["time"] = x_axis
        self.chart_data["x-axis"].append(self.chart_data["time"])
        self.chart_data["y-axis"].append(y_axis)
        if self.chart_data["x-axis"].__len__() >= (data_list_bufor_len + 1):
            self.chart_data["x-axis"].pop(0)
            self.chart_data["y-axis"].pop(0)

    def figure_draw(self,chart_len = 10,  pause = 0.005):

        self.chart_data["axis"].plot(self.chart_data["x-axis"], self.chart_data["y-axis"], color='red')
        self.chart_data["figure"].show()
        plt.pause(pause)

        left = max(0, self.chart_data["time"] - chart_len)
        right = self.chart_data["time"] + 0
        self.chart_data["axis"].set_xlim(left=left, right=right)

    def __del__(self):
        self.chart_data["figure"].clear()
        plt.close()
        print('chart closed')



if __name__ == "__main__":

    chart = Chart()
    chart.chart_attributes(chart_title = 'real time chart', y_axis_name = 'amplitude [inc]', x_axis_name = 'time [s]')

    while True:

        time_start = process_time()


        # sin_wawe(amplitude, offset, period, time)
        output1 = sin_wawe(10, 0, 5, process_time())  # works ok
        output2 = sin_wawe(10, 0, 1, process_time())  # bad refreshment # amplitude, offset, period
        output3 = 2 * process_time() + 5
        output4 = 3 * process_time() + 5

        chart.figure_get_input(y_axis = output2, x_axis = process_time())
        chart.figure_draw(chart_len = 10)

        time_stop = process_time()
        program_execution_time = time_start - time_stop
        print('program_execution_time: {}'.format(program_execution_time))

