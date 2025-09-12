from math import sqrt

def is_prime(n: int):
    if n <= 1:
        return False

    for i in range(2, int(sqrt(n)) +1):
        if n % i == 0:
            return False

    return True

def is_super_prime(n: int):
    if n < 10:
        return is_prime(n)

    return is_prime(n) and is_prime(n // 10)

n = int(input())
print(is_super_prime(n))

