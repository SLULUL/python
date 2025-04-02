def get_weekday(w):
    weekday_map = {'M': '星期一', 'Tu': '星期二', 'W': '星期三',
                   'Th': '星期四', 'F': '星期五', 'Sa': '星期六', 'Su': '星期日'}
    if w[0] in weekday_map:
        return weekday_map[w[0]]
    elif w[0]+w[1] in weekday_map:
        return weekday_map[w[0]+w[1]]
    else:
        return '未找到'


x = 'Tn'
print(f'{get_weekday(x)}')
