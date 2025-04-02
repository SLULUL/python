def fun1(n):
    if n > 1:
        return n * fun1(n - 1)
    else:
        return 1


def fun2(num):
    if num > 1:
        return fun1(num) + fun2(num - 1)
    else:
        return 1


n = 20
print(fun2(20))
