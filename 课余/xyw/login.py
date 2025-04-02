import re
import requests
import socket
import datetime
import time
schoolWebURL = "http://10.200.253.5/"
ip = socket.gethostbyname(socket.gethostname())
print(ip)
# 在下面分别输入你的账号密码，c后面若是电信输入njxy，若是移动输入cmcc，如果用的是TEA网络留空即可。
account = ''
password = ''
c = ''
while True:
    response = requests.get(schoolWebURL)
    pattern = re.compile('<title>(.*?)</title>', re.S)
    title = re.findall(pattern, response.text)
    title = title[0]
    if title == '注销页':
        pass
    else:
        schoolWebLoginURL = schoolWebURL + 'drcom/login?callback=dr1003&DDDDD=' + \
            account + '%40' + c + '&upass=' + password + '&0MKKey=123456'

        response = requests.get(schoolWebLoginURL).status_code

        if (response == 200):
            print(f"{datetime.datetime.now()}:'登陆成功'")
    # time.sleep(0.1)
