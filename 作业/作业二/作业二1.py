d = {'0': 'O', '1': 'I', '2': 'Z', '3': 'E', '4': 'Y', '5': 'S', '6': 'G', '7': 'L', '8': 'B', '9': 'P'}
s = list(input("请输入信息："))
count = 0
for i in s:
    if i in d:
        s[count] = d[i]
    count +=1
print('暗语输出：' + ''.join(s))