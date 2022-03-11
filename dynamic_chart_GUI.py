# author: a5892731
# date: 04.02.2022
# last update: 11.03.2022
# version: 3.0.0
#
# description:
# This is a program that create a dynamic chart

from tkinter import *
from test_files.sin_wawe import sin_wawe
from resources.dynamic_chart_matplotlib import Chartmaker, ChartData
from time import time
from threading import Thread

class ChartWindow:

    def __init__(self, **kwargs):
        self.window = Tk()
        super().__init__()  # import DataExtract variables
        self.window_width = self.window.winfo_screenwidth() - 10
        self.window_height = self.window.winfo_screenheight() - 30
        self.window_variables_init()
        self.set_default()
        self.main_loop()

    def window_variables_init(self):
        self.chart_active = False

        self.data_1 = IntVar()
        self.data_2 = IntVar()
        self.data_3 = IntVar()
        self.data_4 = IntVar()

        self.chart_len = StringVar()
        self.plot_refresh_time = StringVar()
        self.update_data_interval = StringVar()

        self.chart_start_time_Svar = StringVar()
        self.plot_width_Svar = StringVar()
        self.statistic_data_interval_Svar = StringVar()
        self.x_data_len_Svar = StringVar()
        self.y_data_len_Svar  = StringVar()

        self.chart_x_data = 0
        self.chart_y_data = 0

    def set_default(self):
        self.chart_len.set(5)
        self.plot_refresh_time.set(1)
        self.update_data_interval.set(0.01)

        self.data_1.set(1)

    def draw_main_attributes(self):
        self.draw_window_attributes()
        self.main_grid()
        self.draw_chart_window()

    def draw_window_attributes(self):
        self.window.title("dynamic chart starter")
        self.window.geometry("{}x{}".format(self.window_width, self.window_height))

    def main_grid(self):
        self.window.columnconfigure(0, minsize = self.window_width)
        self.window.rowconfigure(0, minsize = self.window_height)
        self.center_frame = LabelFrame(self.window, background="#cfd1cf", bd=5)
        self.center_frame.grid(column=0, row=0,  sticky = "nesw")

    def main_loop(self):
        self.draw_main_attributes()

        while True:
            self.update_data()
            try:
                self.window.update_idletasks()
                self.window.update()
            except:
                print("window closed")
                sys.exit()

    def create_chart_click(self):
        def create_float(str):
            try:
                output = float(str)
            except:
                output = 0.0
            return output

        '''in case of double button click'''
        if self.chart_active == True:
            self.chart.close_figure()  # this function will close all figures.

        '''pre configuration'''
        self.chart_active = True
        self.chart_len_float = create_float(self.chart_len.get())  # seconds
        self.plot_refresh_time_float = create_float(self.plot_refresh_time.get())  # seconds; 0 = MAX POSSIBLE SPEED
        self.update_data_interval_float = create_float(self.update_data_interval.get())
        # update_interval_data [seconds]; 0 = MAX POSSIBLE SPEED

        self.data = ChartData(chart_len_sec=self.chart_len_float)
        self.chart = Chartmaker(chart_active=True,
                                chart_title='test chart', x_name='time [s]', y_name='amplitude [inc]')

        '''prepare data for x (time) axis'''
        self.chart_start_time = time()
        print("create chart")

    def draw_chart_window(self):
        def checkbutton(label, text, variable, column=0, row=0):
            c = Checkbutton(label, font=("Arial", 12), text=text,
                            variable=variable,
                            onvalue=True, offvalue=False, height=0,
                            width=0, background="#cfd1cf",
                            )
            c.grid(column=column, row=row, sticky="wns")

        def draw_entry_line(label, name, variable, row, column=0, unit="[deg]", width=15):
            Label(label, text=name, background="#cfd1cf", bd=5) \
                .grid(column=column, row=row, columnspan=1, sticky="w")
            Entry(label, font=("Arial", 12), textvariable=variable, width=width, ) \
                .grid(column=column, row=row + 1, columnspan=1, sticky="w")
            Label(label, text=unit, background="#cfd1cf", bd=5) \
                .grid(column=column + 1, row=row + 1, columnspan=1, sticky="w")

        def draw_button(label, text, function, column=0, row=0):
            b = Button(label, font=("Arial", 12, "bold"), text=text,
                                    command=function, width=12)
            b.grid(column=column, row=row, sticky="wesn")

        def empty_row(label, column=0, row=0,):
            Label(label, font=("Arial", 12, "bold"), background="#cfd1cf").grid(column=column, row=row, sticky="wesn")

        def chose_data_label_frame(label, column=0, row=0):
            chose_data_label = LabelFrame(label, text="Chose Data To Plot", background="#cfd1cf", bd=5)
            chose_data_label.grid(column=column, row=row, sticky="WESN", )
            #Label(chose_data_label, font=("Arial", 12), text="Chose variable to plot:", background="#cfd1cf", bd=5) \
            #    .grid(column=0, row=0, columnspan=1, sticky="w")
            checkbutton(label=chose_data_label, text="SIN - period 5 s", variable=self.data_1, column=0, row=1)
            checkbutton(label=chose_data_label, text="SIN - period 1 s", variable=self.data_2, column=0, row=2)
            checkbutton(label=chose_data_label, text="SIN - period 500 ms", variable=self.data_3, column=0, row=3)
            checkbutton(label=chose_data_label, text="SIN - period 200 ms", variable=self.data_4, column=0, row=4)

        def command_label_frame(label, column=0, row=0):
            command_label = LabelFrame(label, text="Command", background="#cfd1cf", bd=5)
            command_label.grid(column=column, row=row, sticky="WESN", )

            draw_entry_line(label=command_label, name='plot_refresh_time', variable=self.plot_refresh_time,
                            row=0, column=0, unit="[s]", width=15)
            draw_entry_line(label=command_label, name='chart_len', variable=self.chart_len,
                            row=2, column=0, unit="[s]", width=15)
            draw_entry_line(label=command_label, name='update_data_interval', variable=self.update_data_interval,
                            row=4, column=0, unit="[s]", width=15)
            empty_row(label=command_label, column=0, row=6, )
            draw_button(label=command_label, text='Create Chart', function=self.create_chart_click, column=0, row=7)

        def statistics_label_frame(label, chart_start_time, plot_width, statistic_data_interval, x_data_len, y_data_len,
                                   column=0, row=0):
            statistics_label = LabelFrame(label, text="Chart Statistics", background="#cfd1cf", bd=5)
            statistics_label.grid(column=column, row=row, sticky="WESN", )

            draw_entry_line(label=statistics_label, name='chart time', variable=chart_start_time,
                            row=0, column=0, unit="[s]", width=15)
            draw_entry_line(label=statistics_label, name='plot_width',
                            variable=plot_width,
                            row=2, column=0, unit="[s]", width=15)
            draw_entry_line(label=statistics_label, name='statistic_data_interval',
                            variable=statistic_data_interval,
                            row=4, column=0, unit="[s]", width=15)
            draw_entry_line(label=statistics_label, name='x data len',
                            variable=x_data_len,
                            row=6, column=0, unit="", width=15)
            draw_entry_line(label=statistics_label, name='y data len',
                            variable=y_data_len,
                            row=8, column=0, unit="", width=15)

        plot_label = LabelFrame(self.center_frame, text="Plot Window", background="#cfd1cf", bd=5)
        plot_label.grid(column=0, row=0, sticky="WESN", )

        chose_data_label_frame(label=plot_label, column=0, row=0)
        command_label_frame(label=plot_label, column=1, row=0)
        statistics_label_frame(label=plot_label,
                               chart_start_time=self.chart_start_time_Svar,
                               plot_width=self.plot_width_Svar,
                               statistic_data_interval=self.statistic_data_interval_Svar,
                               x_data_len=self.x_data_len_Svar,
                               y_data_len=self.y_data_len_Svar,
                               column=2, row=0)

    def update_statistic_data(self):
        self.chart_start_time_Svar.set(round(self.chart_x_data,2))
        self.plot_width_Svar.set(round((self.data.x[-1] - self.data.x[0]),3))
        self.statistic_data_interval_Svar.set(round(self.data.statistic_data_interval,3))
        self.x_data_len_Svar.set(len(self.data.x))
        self.y_data_len_Svar.set(len(self.data.y))

    def get_chart_data(self):
        '''prepare data sample for x and y axis'''
        x_data = 0
        y_data = 0

        if self.data_1.get():
            x_data = time() - self.chart_start_time
            y_data = sin_wawe(amplitude=1, offset=0, period=5, time=x_data)  # function to plot
            self.chart.chart_title = 'SIN - period 5 s'

            self.chart.x_name = "time [s]"
            self.chart.y_name = "Pressure [bar]"


        elif self.data_2.get():
            x_data = time() - self.chart_start_time
            y_data = sin_wawe(amplitude=1, offset=0, period=1, time=x_data)  # function to plot
            self.chart.chart_title = 'SIN - period 1 s'
            self.chart.x_name = "time [s]"
            self.chart.y_name = "Voltage [V]"

        elif self.data_3.get():
            x_data = time() - self.chart_start_time
            y_data = sin_wawe(amplitude=1, offset=0, period=0.5, time=x_data)  # function to plot
            self.chart.chart_title = 'SIN - period 500 ms'
            self.chart.x_name = "time [s]"
            self.chart.y_name = "Current [A]"

        elif self.data_4.get():
            x_data = time() - self.chart_start_time
            y_data = sin_wawe(amplitude=1, offset=0, period=0.2, time=x_data)  # function to plot
            self.chart.chart_title = 'SIN - period 200 ms'
            self.chart.x_name = "time [s]"
            self.chart.y_name = "temperature [*C]"

        else:
            x_data = time() - self.chart_start_time
            y_data = 0
            self.chart.chart_title = 'NONE'
            self.chart.x_name = "time [s]"
            self.chart.y_name = "None"


        self.chart_x_data = x_data
        self.chart_y_data = y_data


    def update_data(self):
        def create_float(str):
            try:
                output = float(str)
            except:
                output = 0.0
            return output

        if self.chart_active:
            '''prepare data sample for x and y axis'''
            self.get_chart_data()
            '''update data in window statistics label'''
            self.update_statistic_data()
            '''create threads for data and chart >>>'''
            threads = []
            '''create data array'''
            thread = Thread(target=self.data.update_data(y_data=self.chart_y_data, x_data=self.chart_x_data,
                                                    update_interval_s=self.update_data_interval_float))
            threads.append(thread)
            '''create chart'''
            thread = Thread(target=self.chart.create_figure(x=self.data.x_array, y=self.data.y_array,
                                                       plot_refresh_time=create_float(self.plot_refresh_time.get())))
            threads.append(thread)
            '''start threads'''
            for thread in threads:
                thread.start()
            '''wait for all threads to end'''
            for thread in threads:
                thread.join()
            '''<<< create threads'''

            self.chart_active = self.chart.chart_active
            if self.chart_active == False:
                self.chart.close_figure()  # this function will close all figures.


'''---------------------------------------START APP------------------------------------------------------------------'''
app = ChartWindow()