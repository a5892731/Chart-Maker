from time import process_time, sleep, time

from test_files.sin_wawe import sin_wawe

class ChartData:

    def __init__(self, plot_interval_ms = 100, chart_len_sec = 10):
        '''chart variables'''
        self.plot_interval_ms = plot_interval_ms
        self.elements_for_1000_ms = int(1000 / plot_interval_ms)
        self.elements_in_chart = int(chart_len_sec * self.elements_for_1000_ms)
        self.sample = 1
        '''empty x and y data lists'''
        self.x = [sample / self.elements_in_chart for sample in range(-self.elements_in_chart, 0)]  #chart len in x axis
        self.y = [0 for _ in range(0, self.elements_in_chart)]  # fill the graph with zeros at startup

    def update_data(self, y_data, x_data):
        '''add data to end of the datalists and remove its first element'''
        #time_start = process_time()

        if self.sample * x_data > self.plot_interval_ms / 1000:
            self.sample +=1

            self.x = self.x[1:]  # Remove the first y element.
            self.x.append(x_data)  # Add a new value 1 higher than the last.
            self.y = self.y[1:]  # Remove the first x element.
            self.y.append(y_data)  # Add a new random value.
            #time_stop = process_time()
            #program_execution_time = time_start - time_stop
            #print('program_execution_time: {}'.format(program_execution_time))

'''------------------------------------------------------------------------------------------------------------------'''

if __name__ == '__main__':
    chart_len_sec = 1
    data = ChartData(plot_interval_ms = 100, chart_len_sec = chart_len_sec)
    start_time = time()

    while True:

        x_data = time() - start_time
        y_data = sin_wawe(amplitude=10, offset=0, period=5, time=x_data)  # function to plot

        data.update_data(y_data = y_data, x_data=x_data)


        #print(data.y)
        print(data.x)
        print('current time {} and last element of x {}'.format(x_data, data.x[-1]))
        print('current time - {2} s {0} and first element of x {1} '.format(x_data - chart_len_sec,data.x[0],
                                                                            chart_len_sec))
        print()
        sleep(0.1)