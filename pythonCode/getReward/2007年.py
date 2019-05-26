from urllib import parse

import requests
from bs4 import BeautifulSoup

from getReward import createExcel


# url = "http://www.most.gov.cn/cxfw/kjjlcx/kjjl2000/200802/t20080214_59081.htm"
# html_str = requests.get(url).content.decode("gbk", "replace")
# bs = BeautifulSoup(html_str, "html.parser")
# table = bs.find(name="table", attrs={"class": "MsoTableGrid"})
# tr = table.find_all(name="tr")
# father = []
# for obj in tr:
#     td = obj.find_all(name="td")
#     # print(p)
#     son = []
#     str = ""
#     for obj in td:
#         son.append(obj.text)
#     father.append(son)
# dict = {"MsoTableGrid": father}
# createExcel.create("a1x11as", **dict)

def gteData(url, classAttr, exceName):
    # url = "http://www.most.gov.cn/cxfw/kjjlcx/kjjl2000/200802/t20080214_59081.htm"
    html_str = requests.get(url).content.decode("gbk", "replace")
    print(html_str)
    bs = BeautifulSoup(html_str, "html.parser")
    # bs = BeautifulSoup(html_str, "html5lib")
    # bs = BeautifulSoup(html_str, "lxml")

    dict = {}
    table = bs.findAll(name="table", attrs={"width": "613"})
    i = 0
    for tableObj in table:
        tr = tableObj.find_all(name="tr")
        father = []
        for obj in tr:
            td = obj.find_all(name="td")
            # print(p)
            son = []
            str = ""
            for obj in td:
                print(obj.text)
                # son.append(obj.text)
                p = obj.find_all(name="p")
                if len(p) > 1:
                    for pObj in p:
                        son.append(pObj.text)
                else:
                    son.append(obj.text)
                print("*"*100)
            father.append(son)
        dict.update({classAttr[i]: father})
        i = i + 1
    createExcel.create(exceName, **dict)


url = "http://www.most.gov.cn/ztzl/gjkxjsjldh/jldh2007/jldh07jlgg/200801/t20080108_58277.htm"
# 2002年 一等奖二等奖在两个表格
classAttr = ["一等奖", "二等奖"]
exceName = "2007年度国家科学技术进步奖目录"
gteData(url, classAttr, exceName)


def run():
    url = "http://www.most.gov.cn/ztzl/gjkxjsjldh/jldh2007/jldh07jlgg/200801/t20080108_58277.htm"
    # 2002年 一等奖二等奖在两个表格
    classAttr = ["一等奖", "二等奖"]
    exceName = "2007年度国家科学技术进步奖目录"
    gteData(url, classAttr, exceName)