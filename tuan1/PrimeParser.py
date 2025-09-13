def parse(n):
    i = 2
    factors = []
    term = n

    while i <= term:
        while term % i == 0:
            factors.append(i)
            term //= i
        i += 1

    end = " x ".join(map(str, factors))
    print(f"{n} = {end}")

