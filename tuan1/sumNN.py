# CACH 1
def nn1(n):
    term = 0
    total = 0

    for i in range(1, 5):
        term = term * 10 + n
        total += term

    print(total)

# CACH 2
def nn2(n):
    n = n.strip()

    result = int(n) + int(n*2) + int(n*3) + int(n*4)
    print(result)

n1 = int(input())
n2 = input()
nn1(n1)
nn2(n2)
