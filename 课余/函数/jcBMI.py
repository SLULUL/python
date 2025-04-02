
def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    if bmi <= 18.5:
        return '偏瘦'
    elif 18.5 < bmi <= 25:
        return '正常'
    elif 25 < bmi <= 30:
        return '偏胖'
    else:
        return '肥胖'


if __name__ == '__main__':
    height_input = float(input("请输入身高（米）："))
    weight_input = float(input("请输入体重（千克）："))
    print(calculate_bmi(height_input, weight_input))
