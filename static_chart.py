# author: a5892731
# date: 04.02.2022
# last update: 07.02.2022
# version: 1.3.1
#
# description:
# This program that creates a static charts
#
'''

If you wont to know how to build signal, go to file test_files.static_signals

'''


from test_files.static_signals import SignalMaker
from resources.static_chart import Chartmaker




if __name__ == "__main__":


    signals = SignalMaker()


    charts = Chartmaker(signals.signals)
    #charts = Chartmaker(signals.signals2)

