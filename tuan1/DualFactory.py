def dual_factory(n: int):
    if n == 0:
        return 1

    result = 1
    if n % 2 == 0:
        for i in range(2, n+1, 2):
            result *= i
    else:
        for i in range(1, n+ 1, 2):
            result *= i

    return result

n = int(input())
print(f"{n}!! = {dual_factory(n)}")