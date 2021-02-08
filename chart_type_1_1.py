'''
real time chart:
v.1.1

comments: poor refreshment
'''

import time
import matplotlib.pyplot as plt


def figure_1_1_init():
    x = [0 for i in range(2)] # minimim 2
    y = [0 for i in range(2)] # minimim 2
    fig = plt.figure()
    ax = fig.add_subplot(111)
    return {"figure_data":fig, "figure_data2":ax, "x-axis":x, "y-axis":y, "time":0}

def figure_1_1_input(chart_data, input):
    chart_data["time"] = time.process_time()
    chart_data["x-axis"].append(chart_data["time"])
    chart_data["y-axis"].append(input)
    chart_data["x-axis"].pop(0)
    chart_data["y-axis"].pop(0)
    chart_data = figure_1_1(chart_data)  # realtime chart
    return chart_data

def figure_1_1(chart_data, chart_len = 10):

    def figure_attribute(ax, chart_len, t):
        fig.canvas.draw()
        fig.canvas.set_window_title('SIN')
        plt.title(label = "Chart 1:", fontsize=15, color="black")
        ax.set_xlabel('time')
        ax.set_ylabel('amplitude')
        ax.grid(True)
        fig.show()
        plt.pause(0.01)
        ax.set_xlim(left=max(0, t - chart_len), right=t + 0)

    fig = chart_data["figure_data"]
    ax = chart_data["figure_data2"]
    x = chart_data["x-axis"]
    y = chart_data["y-axis"]
    t = chart_data["time"]

    ax.plot(x, y, color='red')
    figure_attribute(ax, chart_len, t)
    #t = time.process_time()

    return {"figure_data":fig, "figure_data2":ax, "x-axis":x, "y-axis":y, "time":t}
