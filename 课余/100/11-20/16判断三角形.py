s = input("请输入三条边")
x, y, z = map(float, s.split(','))
if x+y > z and x+z > y and y+z > x :
    print("可以是")