import time

user = {}  # 记录账号密码
action = []  # 记录用户行为
status = 0  # 记录登录状态
commodities = []  # 记录购买的商品


def add_action(s):
    action.append(
        f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} {s}")


def sign():
    name = input("请输入你的账号：")
    if name in user.keys():
        print("此用户已存在!")
    else:
        user[name] = input("请输入你的密码：")
        print("注册成功！")
    add_action("注册账号")


def login():
    global status
    if status == 1:
        print("已登录，不用再登录了")
        add_action("在已登录的情况下登录")
        return
    name = input("请输入账号：")
    password = input("请输入密码：")
    if name not in user.keys():
        print("登录失败，账号不存在！")
        add_action("登录账号，但是失败")
        return
    if user[name] == password:
        status = 1
        print('\n登陆成功！')
        add_action("登陆账号")


def shopping():
    global status
    if status == 0:
        print('未登录，请先登录')
        return
    while True:
        add_action("进入购物")
        commodity = input("请输入要购买的商品（输入0退出）：")
        if commodity == '0':
            print("已退出")
            add_action("退出购物")
            return
        commodities.append(commodity)
        print("购买成功！")
        add_action(f"购买{commodity}")


while True:
    print("===================")
    choice = input("请输入进行的操作:\n1:注册\n2:登录\n3:购物\n0:退出\n")
    if choice == '1':
        sign()
    elif choice == '2':
        login()
    elif choice == '3':
        shopping()
    elif choice == '0':
        break
    else:
        print('输入有误，请重新输入')
print('\n用户行为：\n'+'\n'.join(action))
