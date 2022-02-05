from math import pi, sin


def sin_wawe(amplitude, offset, period, time):
    omega = (2 * pi)/period
    return amplitude * sin(omega * time) + offset