def price(d: float) -> float:
    if d <= 2:
        return 13.0
    else:
        return (d-2)*2.6 + 13


if __name__ == '__main__':
    d = float(input("请输入里程数："))
    print(f"本次运行公里数为{d}千米")
    money = price(d)
    print(f"应收取费用：{money: .1f} 元")
    print(f"实收取费用：{round(money)}")
