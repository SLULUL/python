def fun(x):
    if(1000<= x <=10000):
        print(x//1000 + x//100%10*10 + x//10%10*100 + x%10*1000)
    else:
        print("输入错误")

fun(int(input("请输入四位数")))