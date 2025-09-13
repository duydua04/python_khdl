def loan(A, r, n):
    x = A * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

    print("Vay: {:,.2f} Đồng".format(A))
    print("Lãi suất: {:.2f}%/tháng".format(r * 100))
    print("Trong: {:.2f} tháng".format(n))
    print("Mỗi tháng cần trả: {:,.3f} Đồng".format(x))