s = '01，电风扇，台，5，02，洗衣机，T，10，03，商品3，个，15，04，商品4，个，15，05，商品5，伊克萨斯，20，06，微波炉，台，10'
goods = s.split('，')

print("编号\t单价")
for i in range(len(goods) >> 2):
    number = goods[i << 2]
    price = goods[i << 2 | 3]
    print(f"{number}\t{price}")
