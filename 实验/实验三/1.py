'''
以当前日期时间批量创建文件(文本文档)
在平时工作中，我们经常会遇到需要批量创建文件的情况，例如汇总一个月中每天回复问题的文件、储存不同型号产品信息的相应文件等。
解决方案：
(1)保存文件的地址(目录)和创建文件的数量是需要输入的(用input()函数)；
(2)利用datetime模块下的datetime.now()方法获取当前日期时间；
(3)使用strftime()方法对获取到的日期时间进行格式化，作为要创建的文件名；
(4)使用open()方法创建相应的文件。
请根据上面的解决方案编写程序完成要求。
要求：文件的保存地址设置为D:\Test；创建文件的数量设置为10.
'''

import datetime
import os

addr = input("请输入你要保存的地址：")
qty = int(input("请输入你要保存的数量："))
time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
for i in range(1, qty+1):
    file_name = os.path.join(addr, f"{time}_{i}.txt")
    with open(file_name, "w", encoding='utf-8') as file:
        file.write(f"このファイルは{i}番目です")
