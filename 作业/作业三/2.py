def add_people(name: set):
    s = input("请输入人员，以逗号间隔\n")
    n = [x.strip() for x in s.split("，")]
    for i in n:
        name.add(i)
    print("添加成功！")


s = set()
while True:
    choice = input("\n统计名单：\n请选择 1：添加人员 2：查询名单 0：退出\n")
    if choice == '1':
        add_people(s)
    elif choice == '2':
        print(s)
    elif choice == '0':
        break
    else:
        print("输入有误，请重新输入")
