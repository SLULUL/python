import random
import string

# 设置随机种子保证可重复性
random.seed(42)

def random_demo():
    """展示random模块常用功能"""
    
    # 1. 生成随机整数
    print("1. 随机整数:")
    print(f"   - 范围0-10: {random.randint(0, 10)}")
    print(f"   - 范围5-15: {random.randint(5, 15)}")
    
    # 2. 生成随机浮点数
    print("\n2. 随机浮点数:")
    print(f"   - 0-1之间: {random.random():.3f}")
    print(f"   - 1.5-3.5之间: {random.uniform(1.5, 3.5):.3f}")
    
    # 3. 列表随机操作
    fruits = ['apple', 'banana', 'cherry', 'durian', 'elderberry']
    print("\n3. 列表操作:")
    print(f"   - 随机选择: {random.choice(fruits)}")
    print(f"   - 随机选取多个: {random.sample(fruits, k=3)}")
    
    # 4. 打乱列表顺序
    cards = ['A', '2', '3', '4', '5', 'J', 'Q', 'K']
    random.shuffle(cards)
    print(f"   - 洗牌结果: {cards}")
    
    # 5. 生成随机字符串
    print("\n4. 随机字符串:")
    letters = random.choices(string.ascii_uppercase, k=5)
    print(f"   - 大写字母: {''.join(letters)}")
    
    # 6. 概率分布示例
    print("\n5. 正态分布:")
    normal_values = [round(random.gauss(0, 1), 2) for _ in range(5)]
    print(f"   - 正态分布值: {normal_values}")

if __name__ == "__main__":
    random_demo()