import re
s = '2018 Amazon Jeff Bezos 1120'
s1 = '要么创新，要么杰夫贝索斯帮你创新'

# 去掉'2018 '
print(s.replace('2018 ', ''))

# 提取数字
print(''.join(re.findall(r'\d', s)))

# 数字加【】
print(re.sub(r'\s*(\d+)\s*', r'【\1】', s))

# 去除空格
print(s.replace(' ', ''))

# 数字乘两倍
print(re.sub(r'\d+', lambda x: str(int(x.group()) << 1), s))

# 添加字符串
print(s1.replace('杰夫贝索斯', '杰夫贝索斯(Jeff Bezos)'))
