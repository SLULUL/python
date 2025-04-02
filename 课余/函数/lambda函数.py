g = lambda x: x*g(x-1) if (x>1) else 1 #递归出阶乘
print(g(5))