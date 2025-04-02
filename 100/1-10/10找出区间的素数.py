import math
def fun1(num):
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True
def fun2(num1, num2):
    for i in range(num1, num2+1):
        if fun1(i):
            print(i)
fun2(2, 100)