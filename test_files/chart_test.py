class ChartTests:
    def __init__(self,):
        self.chart_sample = 1

    def print_test_data(self, ChartClass, program_execution_time):
        chart = ChartClass

        if chart.chart_sample > self.chart_sample:
            self.chart_sample += 1

            print('sample : nr {}'.format(chart.chart_sample))
            print('chart time: {} s'.format(round(chart.chart_time_ms / 1000, 3)))
            print('program_execution_time_when_printing_chart: {} s'.format(round(program_execution_time, 3)))
            print('---------------------------------------------------------------------')