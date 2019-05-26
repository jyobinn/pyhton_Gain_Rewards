import re
from time import sleep

import requests
from bs4 import BeautifulSoup

from pythonUrllibDemo.Area import Area
from pythonUrllibDemo.Tools import getBytes

url = "https://xingzhengquhua.51240.com/110101001001__xingzhengquhua/"
html = requests.get(url)
html_bytes = html.content
html_str = html_bytes.decode()
print("qqqqqqqqqqqqqqqqqqqqqqqqqqq"*100)
print(html_str)

# bs = BeautifulSoup(html_str, "html.parser")
# i = 0
# area = None
# areaList = []
# for item in bs.find_all("a", href=re.compile('_xingzhengquhua')):
#     if i % 2 == 0:
#         # url
#         # print(item['href'][0: -1])
#         # 地区名字
#         # print(item.text)
#         area = Area(item.text, url[0: -1] + item['href'])
#     else:
#         # 地区code
#         # print(item.text)
#         area.setUrl(item.text)
#     areaList.append(area)
#     i = i + 1

# print(len(areaList))

# if len(areaList) > 0:
#     for obj in areaList:
#         areaList2 = getBytes(obj.url)
#         sleep(3)

# https://xingzhengquhua.51240.com/110000000000__xingzhengquhua/
# https://xingzhengquhua.51240.com/520000000000__xingzhengquhua

# getBytes("https://xingzhengquhua.51240.com/110101001000__xingzhengquhua/")