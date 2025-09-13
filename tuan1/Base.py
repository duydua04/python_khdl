from math import sqrt


def isPerfectNumber(number: int):
    """
    Số hoàn hảo là một số nguyên dương mà tổng các ước nguyên dương thực sự của nó
    (các ước nguyên dương ngoại trừ chính số đó) bằng chính nó. Hoàn thiện hàm isPerfectNumber(number)
    nhận vào số nguyên dương number và trả về True nếu number là số hoàn hảo
    và False nếu number không phải là số hoàn hảo.

    Ví dụ:
    input: 6
    ouput: True

    input: 14
    output: False
    """
    if number <= 1:
        return False

    tong_uoc = 1
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            tong_uoc += i
            j = number // i
            if j != i:
                tong_uoc += j

    return tong_uoc == number


def drawPatterm(height: int):
    """
    Hãy vẽ hình vuông có chiều cao height.
    Ví dụ
    input: 4
    output:
    ****
    *  *
    *  *
    ****
    """
    ...
    if height <= 0:
        return
    if height == 1:
        print("*")
        return

    print("*" * height)

    for _ in range(height - 2):
        print("*" + " " * (height - 2) + "*")

    print("*" * height)

def caculateExp(x: float, n: int):
    """
    Hoàn thiện hàm tính e^x theo công thức đã cho của đề bài.
    Ví dụ:
    input: 2 100 (Tương ứng x = 2 và n = 100)
    output: 7.3890561
    """
    if n < 0:
        pass

    s = 1
    term = 1

    for i in range(1, n+ 1):
        term *= (x/i)
        s += term

    return s