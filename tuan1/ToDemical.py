
def convert(n):
    n = n.strip()
    decimal = 0

    for i, bit in enumerate(reversed(n)):
        decimal += int(bit) * (2**i)

    return decimal