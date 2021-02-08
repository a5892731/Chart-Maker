import time
import psutil
import matplotlib.pyplot as plt
from sin_wawe import sin_wawe


def figure_1():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    t = 0.0
    x, y = [], []
    amplitude = 10
    offset = 0
    period = 10
    chart_len = 10

    while True:

        x.append(t)
        y.append(sin_wawe(amplitude, offset, period, t))

        ax.plot(x, y, color='b')

        fig.canvas.draw()
        fig.canvas.set_window_title('SIN')
        ax.set_xlim(left=max(0, t - chart_len), right= t + 0)
        ax.set_xlabel('time')
        ax.set_ylabel('amplitude')
        ax.grid(True)

        fig.show()
        plt.pause(0.05)
        t = time.process_time()

if __name__ == "__main__":
    figure_1()