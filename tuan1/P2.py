from math import sqrt

def solver(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                print("VSN")
            else:
                print("VN")
        else:
            print(-c/b)
    else:
        delta = b**2 - 4*a*c

        if delta < 0:
            print("VN")
        elif delta == 0:
            print(-b/(2*a))
        else:
            x1 = (-b - sqrt(delta))/(2*a)
            x2 = (-b + sqrt(delta))/(2*a)
            print(f"{x1} {x2}")


