def get_valid_name(prompt):
    """获取有效的中文姓名输入"""
    while True:
        name = input(prompt).strip().replace(' ', '').replace('·', '')
        if not name:
            print("输入不能为空！")
            continue
        if all('\u4e00' <= c <= '\u9fff' for c in name):
            return name
        print("请输入有效的中文字符！")

def calculate_name_difference():
    """计算两个中文姓名的编码差异"""
    try:
        print("【第一位信息】")
        person1_surname = get_valid_name("请输入姓氏：")
        person1_givenname = get_valid_name("请输入名字：")
        
        print("\n【第二位信息】")
        person2_surname = get_valid_name("请输入姓氏：")
        person2_givenname = get_valid_name("请输入名字：")

        # 计算全名编码（姓氏权重加倍）
        def calc_fullname_code(surname, givenname):
            return sum(ord(c) for c in surname)*2 + sum(ord(c) for c in givenname)
            
        code1 = calc_fullname_code(person1_surname, person1_givenname)
        code2 = calc_fullname_code(person2_surname, person2_givenname)
        
        # 将差异标准化到0-100范围
        max_diff = 2000  # 基于常见中文姓名的预估最大值
        diff = min(abs(code1 - code2), max_diff)
        return round(diff / max_diff * 100, 1)
    except Exception as e:
        print(f"发生错误：{e}")
        return None

if __name__ == "__main__":
    result = calculate_name_difference()
    if result is not None:
        print(f"计算结果为：{result}")