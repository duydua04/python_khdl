# giải phương trình f(x) = 0, tìm nghiệm xấp xỉ c theo phương pháp chia đôi.
from math import fabs as abs

def solver(f, a, b, e=0.000001):
    fa = f(a)
    fb = f(b)

    if fa == 0:
        return a
    if fb == 0:
        return b

    for _ in range(100000):
        c = (a + b) / 2.0
        fc = f(c)

        if abs(fc) <= e:
            return c

        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc

    return (a + b) / 2.0
