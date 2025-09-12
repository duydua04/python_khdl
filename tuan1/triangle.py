# Viết chương trình tính chu vi và diện tích tam giác
from math import sqrt

def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False

    return a + b > c and a + c > b and b + c > a

a = float(input())
b = float(input())
c = float(input())

if not is_triangle(a, b, c):
    print("INVALID")
else:
    C = a + b + c
    p = C / 2
    S = sqrt(p*(p-a)*(p-b)*(p-c))

    print(f"S =  {S} C =  {C}")