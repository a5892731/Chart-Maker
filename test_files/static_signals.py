import numpy as np

class SignalMaker:
    def __init__(self):
        dt = 0.01
        t1 = np.arange(0, 50, dt)  #time interval and sample: from 0 to 50 by 0.01
        s1 = np.sin(2 * np.pi * 0.2 * t1)
        t2 = np.arange(0, 50, dt)
        s2 = np.sin(2 * np.pi * 0.1 * t2)
        t3 = np.arange(-20, 20, dt)
        s3 = -(pow((10 * t3), 2)) + 500
        t4 = np.arange(-20, 20, dt)
        s4 = (10 * t4)
        t5 = np.arange(-20, 20, dt)
        s5 = -(10 * t5)

        '''self.signals = {'chart_1':{'singal_1': {'x': s1, 'y':t1},
                                   'singal_2': {'x': s2, 'y':t2},
                                   'x_name':'time [s]',
                                   'x_range': [0, 50],
                                   'y_name': 'amplituda [inc]',
                                   'y_range': [-1, 1],
                                   },
                        'chart_2':{'singal_3': {'x': s3, 'y':t3},
                                   #'singal_4': {'x': s4, 'y':t4},
                                   #'singal_5': {'x': s5, 'y':t5},
                                   'x_name': 'time [s]',
                                   'x_range': [-20, 20],
                                   'y_name': 'amplituda [inc]',
                                   'y_range': [-600, 600],
                                   },

                        }'''

        self.signals = {'chart_1':{'singal_1': {'x': s1, 'y':t1},
                                   'x_name':'time [s]',
                                   'x_range': [0, 50],
                                   'y_name': 'amplituda [inc]',
                                   'y_range': [-1, 1],
                                   },
                        }
