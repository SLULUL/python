'''
获取NBA球员收入信息表格数据
网址为：
http://www.espn.com/nba/salaries/_/seasontype/4
    请通过Pandas的read_html()方法获取网页数据，抽取里面前10项数据，保存为.csv文件。
'''
import pandas as pd

url = 'http://www.espn.com/nba/salaries/_/seasontype/4'
df = pd.read_html(url)[0]
top_10 = df.iloc[1: 11]
top_10.to_csv('nba.csv', index=False)

print("数据已成功保存为nba.csv")
