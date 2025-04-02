score = int(input("请输入成绩"))
if (90 <= score <= 100):
    print("A")
elif (60 <= score <= 89):
    print("B")
elif (0 <= score <= 59):
    print("C")
else:
    print("输入有误")
