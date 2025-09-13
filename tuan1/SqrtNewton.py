from math import sqrt

def sqrt_newton(c):
    EPSILON = 1e-15
    t = c

    while abs(t - c/t) > EPSILON * t:
        if t == c / t:
            t = sqrt(c)
        else:
            t = (t + c/t) / 2

    return t