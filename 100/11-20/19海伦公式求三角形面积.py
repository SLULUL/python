import math
def fun(x, y ,z):
    p = (x + y + z) / 2
    S = math.sqrt(p * (p - x) * (p - y) * (p -z))
    return S
print(fun(3, 4, 5))