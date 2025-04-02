f = lambda d : d * 9.912
g = lambda d : d * 0.1009
while True:
    t = input("请选择\n输入1：人民币转卢布\n2：卢布转人民币\n0：退出\n")
    if t == '1':
        print("卢布：%f" %f(float(input("请输入人民币："))))
    elif t == '2':
        print("人民币：%f" %f(float(input("请输入卢布："))))
    elif t == '0':
        break
    else:
        print("输入有误，请重新输入")