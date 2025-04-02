def fun(num):
    if(num == 1):
        return 1
    else:
        return num * fun(num-1)
print(fun(5))