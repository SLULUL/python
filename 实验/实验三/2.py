import os

# 手机型号列表
products = [
    "小米10Pro",
    "OPPO FindX2",
    "iPhone 12mini",
    "华为P40Pro",
    "小米10至尊纪念版",
    "iPhone 12",
    "华为Mate40Pro",
    "iPhone 12 MaxPro",
    "红米K30Pro",
    "OPPO Ace2"
]
os.makedirs("D:\\Test1", exist_ok=True)
if not os.path.exists("D:\\Test1\\product.txt"):
    with open("D:\\Test1\\product.txt", "w", encoding='utf-8') as f:
        f.write("\n".join(products))

with open("D:\\Test1\\product.txt", "r", encoding='utf-8') as file:
    r = file.readlines()
    for i in range(len(r)):
        os.mkdir(f"D:\\Test1\\{r[i].strip()}")
