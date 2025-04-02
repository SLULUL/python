l = list(input("请输入字符串："))
num = char = spa = other = 0
# for i in l:
#     if ord('1') <= ord(i) <= ord('9'):
#         num += 1
#     elif ord('a') <= ord(i) <= ord('z') or ord('A') <= ord(i) <= ord('Z'):
#         str += 1
#     else:
#         other += 1
for i in l:
    if i.isdigit():
        num += 1
    elif i.isalpha():
        char += 1
    elif i.isspace():
        spa += 1
    else:
        other += 1
print(f"数字：{num} 字母：{char} 空格：{spa} 其他：{other}")
