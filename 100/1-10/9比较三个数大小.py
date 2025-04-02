def compare_three(a, b, c):
    # 先比较前两个数
    max_num = a if a > b else b
    # 再比较临时最大值和第三个数
    return max_num if max_num > c else c

if __name__ == "__main__":
    # 测试用例
    print(compare_three(10, 20, 30))  # 应输出30
    print(compare_three(-5, 0, 5))    # 应输出5
    print(compare_three(5, 5, 5))     # 应输出5
