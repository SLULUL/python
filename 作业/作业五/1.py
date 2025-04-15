import time


class User:
    def __init__(self):
        self.accounts = {}  # 账号密码存储
        self.logged_in = False  # 登录状态
        self.actions = []  # 用户行为记录

    def add_action(self, action):
        self.actions.append(
            f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} {action}")

    def register(self):
        name = input("请输入你的账号：")
        if name in self.accounts:
            print("此用户已存在!")
        else:
            self.accounts[name] = input("请输入你的密码：")
            print("注册成功！")
        self.add_action("注册账号")

    def login(self):
        if self.logged_in:
            print("已登录，不用再登录了")
            self.add_action("在已登录的情况下登录")
            return

        name = input("请输入账号：")
        password = input("请输入密码：")
        if name not in self.accounts:
            print("登录失败，账号不存在！")
            self.add_action("登录账号，但是失败")
            return

        if self.accounts[name] == password:
            self.logged_in = True
            print('\n登陆成功！')
            self.add_action("登陆账号")
        else:
            print("密码错误！")


class ShoppingSystem:
    def __init__(self, user):
        self.user = user
        self.commodities = []  # 购买的商品

    def shopping(self):
        if not self.user.logged_in:
            print('未登录，请先登录')
            return

        while True:
            self.user.add_action("进入购物")
            commodity = input("请输入要购买的商品（输入0退出）：")
            if commodity == '0':
                print("已退出")
                self.user.add_action("退出购物")
                return
            self.commodities.append(commodity)
            print("购买成功！")
            self.user.add_action(f"购买{commodity}")


def main():
    user = User()
    shopping_system = ShoppingSystem(user)

    while True:
        print("===================")
        choice = input("请输入进行的操作:\n1:注册\n2:登录\n3:购物\n0:退出\n")

        if choice == '1':
            user.register()
        elif choice == '2':
            user.login()
        elif choice == '3':
            shopping_system.shopping()
        elif choice == '0':
            break
        else:
            print('输入有误，请重新输入')

    print('\n用户行为：\n'+'\n'.join(user.actions))


if __name__ == "__main__":
    main()
