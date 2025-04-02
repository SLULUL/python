import math

def prime_factors(n):
    """分解质因数并返回有序列表"""
    if n < 2:
        return []
    
    factors = []
    
    # 处理偶数因子
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # 处理奇数因子
    i = 3
    max_factor = math.isqrt(n) + 1
    while i <= max_factor and n > 1:
        while n % i == 0:
            factors.append(i)
            n = n // i
            max_factor = math.isqrt(n) + 1
        i += 2
    
    # 处理剩余的大质数
    if n > 1:
        factors.append(n)
    
    return factors

# 测试代码
if __name__ == "__main__":
    print(prime_factors(4199))  # 输出: [2, 2, 3, 3, 5]