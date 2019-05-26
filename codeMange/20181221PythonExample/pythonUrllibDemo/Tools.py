import re

import requests
from bs4 import BeautifulSoup

from pythonUrllibDemo.Area import Area


def getBytes(url):
    print(url)
    html = requests.get(url)
    html_bytes = html.content
    html_str = html_bytes.decode()
    print("strart")
    # print(html_str)
    print("end")
    bs = BeautifulSoup(html_str, "html.parser")
    table_node = bs.find_all("td", bgcolor="#FFFFFF")
    print(len(table_node))
    # table_node2 = bs.find_all("td", bgcolor="#FFFFFF")
    # print(list(table_node2.difference(table_node)))
    # set(table_node2)-set(table_node)
    # print(len(table_node))
    list = []
    for table in table_node:
        print(table.get("colspan"))
        if table.get("colspan") == None:
            list.append(table)
        # table.get_text()
    print(list)
    i = 0
    area = None
    areaList = []
    for item in bs.find_all("a", href=re.compile('_xingzhengquhua')):
        if i % 3 == 0:
            # url
            # print(item['href'][0: -1])
            # 地区名字
            # print(item.text)
            # area = Area(item.text, url[0: -1] + item['href'])
            print()
        elif i % 3 == 0:
            pass
        else:
            pass
            # 地区code
            # print(item.text)
            # area.setUrl(item.text)
        # areaList.append(area)
        i = i + 1
    # print(len(areaList))
    return areaList


getBytes("https://xingzhengquhua.51240.com/110101001000__xingzhengquhua/")