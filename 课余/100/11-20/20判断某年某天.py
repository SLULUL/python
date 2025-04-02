import datetime
x, y, z = map(int,(input("请输入年:月:日")).split(':'))
delta = datetime.date(x, y, z) - datetime.date(x, 1, 1)
print(f"{delta.days}days")  # 移除了所有格符号's'