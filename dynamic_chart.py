'''
real time chart:

comments: poor refreshment
'''

import time
import matplotlib.pyplot as plt

class chart():
    version = "1.2"
    chart_title = "Chart 1:"
    chart_len = 10
    data_list_bufor_len = 2 # minimum 2
    #chart_data = {}

    def __init__(self):
        x = [0 for i in range(self.data_list_bufor_len)]
        y = [0 for i in range(self.data_list_bufor_len)]
        fig = plt.figure()
        ax = fig.add_subplot(111)
        self.chart_data = {"figure": fig, "axis": ax, "x-axis": x, "y-axis": y, "time": 0}

    def figure_get_input(self, input):
        self.chart_data["time"] = time.process_time()
        self.chart_data["x-axis"].append(self.chart_data["time"])
        self.chart_data["x-axis"].pop(0)
        self.chart_data["y-axis"].append(input)
        self.chart_data["y-axis"].pop(0)

    def figure_draw(self):
        self.chart_data["axis"].plot(self.chart_data["x-axis"], self.chart_data["y-axis"], color='red')

        self.chart_data["figure"].canvas.draw()
        self.chart_data["figure"].canvas.set_window_title('SIN')
        plt.title(label=self.chart_title, fontsize=15, color="black")
        self.chart_data["axis"].set_xlabel('time')
        self.chart_data["axis"].set_ylabel('amplitude')
        self.chart_data["axis"].grid(True)
        self.chart_data["figure"].show()
        plt.pause(0.01)
        self.chart_data["axis"].set_xlim(left=max(0, self.chart_data["time"] - self.chart_len),
                                        right=self.chart_data["time"] + 0)



