'''
version 1.3.1
'''


from test_files.static_signals import SignalMaker
import matplotlib.pyplot as plt


class Chartmaker:

    def __init__(self, charts ):
        self.charts = charts
        self.axs = list() # list of axis
        self.create_chart()
        self.create_figure()

    def create_chart(self):
        if len(self.charts) > 1:
            self.fig, self.axs = plt.subplots(len(self.charts), 1)  # ilosć wykresów
        else:
            self.fig, self.axis = plt.subplots()
            self.axs.append(self.axis) # axis data must be a list in this program -
                                       # because you can have more than 1 chart in this program
    def create_figure(self):
        chart_number = 0
        for chart in self.charts:

            for signal in self.charts[chart]:
                if signal != 'x_name' and signal != 'x_range' and signal != 'y_name' and signal != 'y_range':
                    #print(chart, signal)
                    #print(self.signals[chart]['x_range'][0], self.signals[chart]['x_range'][1])
                    #print(len(self.signals[chart][signal]['y']), len(self.signals[chart][signal]['x']), )
                    self.axs[chart_number].plot(self.charts[chart][signal]['y'], self.charts[chart][signal]['x'])

            self.axs[chart_number].set_title(chart)
            self.axs[chart_number].set_xlim(self.charts[chart]['x_range'][0], self.charts[chart]['x_range'][1])
            self.axs[chart_number].set_ylim(self.charts[chart]['y_range'][0], self.charts[chart]['y_range'][1])
            self.axs[chart_number].set_xlabel(self.charts[chart]['x_name'])
            self.axs[chart_number].set_ylabel(self.charts[chart]['y_name'])
            self.axs[chart_number].grid(True)
            chart_number += 1

        self.fig.tight_layout()
        plt.show()

if __name__ == "__main__":

    signals = SignalMaker()
    charts = Chartmaker(signals.signals)


