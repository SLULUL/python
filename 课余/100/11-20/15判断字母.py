while True:
    s = input("请输入字符")
    if len(s) >= 2 :
        print("非字符，请重新输入")
        continue
    if 65<= ord(s) <=90 or 97<= ord(s) <=122:
        print("是字母")
    else:
        print("不是字母")