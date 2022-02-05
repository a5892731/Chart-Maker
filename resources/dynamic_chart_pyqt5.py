'''

works fine, but it should get data in different way.


'''

from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot, mkPen
import sys  # We need sys so that we can pass argv to QApplication
from time import process_time, time, sleep
from random import randint

from test_files.sin_wawe import sin_wawe


class Chart(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(Chart, self).__init__(*args, **kwargs)

        '''create plot'''
        self.graphWidget = PlotWidget()
        self.setCentralWidget(self.graphWidget)
        '''set main attributes of chart'''
        #self.get_chart_attributes()
        '''system variables'''
        self.start_time = time()

    def get_chart_attributes(self, chart_len_sec = 10, line_rgb=(0, 0, 255), background = 'white',
                            x_axis_name = 'temperature [°C]', y_axis_name = 'time [s]',
                            chart_title = "Czujnik Temperatury 1", plot_interval_ms = 100):
        '''function sets chart atributes'''
        '''chart variables'''
        self.plot_interval_ms = plot_interval_ms
        elements_for_1000_ms = int(1000 / plot_interval_ms)
        elements_in_chart = int(chart_len_sec * elements_for_1000_ms)
        '''chart settings'''
        self.x = [sample/elements_in_chart for sample in range(-elements_in_chart, 0)] # chart len in x axis
        self.y = [0 for _ in range(0, elements_in_chart)]  # fill the graph with zeros at startup
        self.graphWidget.setBackground(background) # background color
        pen = mkPen(color=line_rgb, width=2) # color of the line in RGB - Red Green Blue ->  (0, 0, 255) blue
        #https://www.w3schools.com/colors/colors_rgb.asp
        self.data_line = self.graphWidget.plot(self.x, self.y, pen=pen)
        self.graphWidget.setLabel('left', "<span style=\"color:black;font-size:15px\">{0}</span>".format(x_axis_name))
        self.graphWidget.setLabel('bottom', "<span style=\"color:black;font-size:15px\">{0}</span>".format(y_axis_name))
        self.graphWidget.setTitle("<span style=\"color:black;font-size:20pt\">{0}</span>".format(chart_title))

    def chart_auto_updater(self, function):
        '''function is automatically  updating a chart with interval (50 ms) with data from: function called
        from signed row'''
        self.timer = QtCore.QTimer()
        self.timer.setInterval(self.plot_interval_ms)
        self.timer.timeout.connect(function)  #signed row: callfunction lambda: function(x, y)
        self.timer.start()


    def update_plot_data_test(self):
        '''random plot for testing'''
        #time_start = process_time()
        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.
        self.y = self.y[1:]  # Remove the first
        self.y.append(randint(0, 100))  # Add a new random value.
        self.data_line.setData(self.x, self.y)  # Update the data.
        #time_stop = process_time()
        #program_execution_time = time_start - time_stop
        #print('program_execution_time: {}'.format(program_execution_time))

    def update_plot_data(self):
        '''plot a function'''
        x_data = (time() - self.start_time)

        y_data = sin_wawe(amplitude = 10, offset = 0, period = 5, time = x_data)   # function to plot

        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(x_data)  # Add a new value 1 higher than the last.
        self.y = self.y[1:]  # Remove the first
        self.y.append(y_data)  # Add a new random value.
        self.data_line.setData(self.x, self.y)  # Update the data.

    def __del__(self):
        print("chart closed")




'''------------------------------------------------------------------------------------------------------------------'''
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    chart = Chart()
    chart.get_chart_attributes(chart_len_sec=10, line_rgb=(0, 0, 255), background='white',
                               x_axis_name='temperature [°C]', y_axis_name='time [s]',
                               chart_title="Czujnik Temperatury 1", plot_interval_ms=100)
    chart.show()

    chart.chart_auto_updater(chart.update_plot_data)

    sys.exit(app.exec_())