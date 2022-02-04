import math


def sin_wawe(amplitude, offset, period, time):
    omega = (2 * math.pi)/period
    return amplitude * math.sin(omega * time) + offset