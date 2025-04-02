n = int(input("请输入一个数字: "))
s = str(n)
b = True
for i in range(len(s)//2):
    if s[i] != s[len(s)-i-1]:
        b = False
        break
if b:
    print(f"{n} 是回文数")
else:
    print(f"{n} 不是回文数")
