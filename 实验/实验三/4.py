'''
读取time.xls文件，抽取前20个会员的信息，提取他们的会员名、宝贝标题和订单付款时间的信息，保存为.xlsx文件。
'''
import pandas as pd
data = pd.read_excel('实验/实验三/time.xls', sheet_name='Sheet1')
top20 = data.head(20)
result = top20[['买家会员名', '宝贝标题 ', '订单付款时间']]
result.to_excel('实验/实验三/top20.xlsx', index=False)
print("成功提取并保存前20个会员信息到top20.xlsx")
print("数据预览：")
print(result.head())
