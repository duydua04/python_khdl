from math import fmod, pi

def sinTaylor(x):
    y = fmod(x, 2*pi)

    s = 0.0
    term = y
    k = 0
    while term != 0.0:
        s += term
        k += 1
        term *= - y*y / ((2*k) * (2*k + 1))
    return s


def cosTaylor(x):
    y = fmod(x, 2*pi)

    s = 0.0
    term = 1.0
    k = 0
    while term != 0.0:
        s += term
        k += 1
        term *= - y*y / ((2*k - 1) * (2*k))
    return s
