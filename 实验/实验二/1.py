def fun(n: int, j: int) -> str:
    if n == 0:
        return "0"
    lst = []
    while n > 0:
        r = n % j
        if r < 10:
            lst.append(str(r))
        else:
            lst.append(chr(ord('A') + r - 10))
        n = n // j
    return ''.join(reversed(lst))


if __name__ == '__main__':
    num1 = int(input("请输入一个十进制整数"))
    print(f"{num1}的二进制为{bin(num1)}，八进制为{oct(num1)}，十六进制为{hex(num1)}")
    j = int(input("请输入你要转换的进制"))
    print(f"{num1}转换为{j}进制为{fun(num1, j)}")
