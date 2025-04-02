height = 100  # 初始高度
total = 100    # 总路程（第一次落地）

for _ in range(9):  # 后续9次弹起+落地
    height /= 2
    total += height * 2  # 每次弹起和落下都要计算

print(f"第10次落地时共经过：{total:.3f}米")
print(f"第10次反弹高度：{height/2:.4f}米")
