import re
import requests
import time
from lxml import etree
# 设置url
url = 'https://www.ddyveshu.cc/1_1641/41295475.html'
while True:

    # 延迟1s防止服务器无响应
    time.sleep(1)

    # 伪装为chrome浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    }

    # 发送请求
    resp = requests.get(url, headers=headers)

    # 设置编码
    resp.encoding = 'GBK'

    # 响应信息
    # print(resp.text)
    e = etree.HTML(resp.text)
    info = e.xpath('//*[@id="content"]/text()')
    title = e.xpath('//div/h1/text()')

    # 清洗文本内容（deepseek写的）
    cleaned_info = []
    for paragraph in info:
        # 去除全角空格和转义字符
        p = re.sub(r'[\u3000\r\n]', '', paragraph)
        # 移除首尾空白
        p = p.strip()
        if p:  # 过滤空段落
            cleaned_info.append(p)

    # 合并段落并添加换行
    formatted_text = '\n\n'.join(cleaned_info)

    print(f"章节标题：{title[0]}")
    # print("------ 正文内容 ------")
    # print(formatted_text)

    # 下一次循环为下一章url
    url = 'https://www.ddyveshu.cc' + e.xpath(
        '//div[2]/div[1]/a[3]/@href')[0]

    # 写入文件（'a'是追加，'w'是覆盖，'r'是只读）
    with open('项目\爬虫\斗罗大陆.txt', 'a', encoding='UTF-8') as f:
        f.write(title[0] + '\n\n' + formatted_text + '\n\n')

    # 退出循环，当下次url为目录时结束循环
    if url == 'https://www.ddyveshu.cc/1_1641/':
        break
