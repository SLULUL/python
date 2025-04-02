l = [["有座" for _ in range(5)] for _ in range(13)]
print('\n'.join(' '.join(m) for index, m in enumerate(l)))
while True:
    s = input("请输入购买的座位位置（格式：排号,列号）：")
    x, y = map(int, s.split(','))
    if(0<=x<=13 and 0<=y<=5):
        l[x-1][y-1] = "已售"
        print("更新后的座位表：\n"+'\n'.join(' '.join(m) for m in l))
    else:
        print("输入有误！")