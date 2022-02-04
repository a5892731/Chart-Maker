from test_files.static_signals import SignalMaker
import matplotlib.pyplot as plt


class Chartmaker:

    def __init__(self, signals ):
        self.signals = signals

        self.create_figure()

    def create_figure(self):
        self.fig, self.axs = plt.subplots(len(self.signals), 1)  # ilosć wykresów

        chart_number = 0
        for chart in self.signals:

            for signal in self.signals[chart]:
                if signal != 'x_name' and signal != 'x_range' and signal != 'y_name' and signal != 'y_range':
                    #print(chart, signal)
                    #print(self.signals[chart]['x_range'][0], self.signals[chart]['x_range'][1])
                    #print(len(self.signals[chart][signal]['y']), len(self.signals[chart][signal]['x']), )
                    self.axs[chart_number].plot(self.signals[chart][signal]['y'], self.signals[chart][signal]['x'])

            self.axs[chart_number].set_title(chart)
            self.axs[chart_number].set_xlim(self.signals[chart]['x_range'][0], self.signals[chart]['x_range'][1])
            self.axs[chart_number].set_ylim(self.signals[chart]['y_range'][0], self.signals[chart]['y_range'][1])
            self.axs[chart_number].set_xlabel(self.signals[chart]['x_name'])
            self.axs[chart_number].set_ylabel(self.signals[chart]['y_name'])
            self.axs[chart_number].grid(True)
            chart_number += 1

        self.fig.tight_layout()
        plt.show()




if __name__ == "__main__":

    signals = SignalMaker()
    charts = Chartmaker(signals.signals)


