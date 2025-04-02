def add_contact(contacts):
    name = input("姓名：")
    if name in contacts:
        print("联系人已存在")
        return
    phone = input("电话：")
    contacts[name] = phone
    print("添加成功")


def query_contact(contacts):
    key = input("查询姓名或电话：")
    results = {k: v for k, v in contacts.items()
               if key in k or key in v}

    if results:
        print("\n查询结果：")
        for name, phone in results.items():
            print(f"{name}: {phone}")
    else:
        print("未找到联系人")


def del_contact(contacts):
    name = input("删除联系人姓名：")
    if name in contacts:
        del contacts[name]
        print("删除成功")
    else:
        print("联系人不存在")


if __name__ == '__main__':
    contacts = {}
    while True:
        print("\n手机通讯录")
        choice = input("请选择: 1添加 2查询 3删除 0退出\n")

        if choice == '1':
            add_contact(contacts)

        elif choice == '2':
            query_contact(contacts)

        elif choice == '3':
            del_contact(contacts)

        elif choice == '0':
            print("已退出")
            break

        else:
            print("输入有误，请重新输入")
