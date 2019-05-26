from urllib import parse

import requests
from bs4 import BeautifulSoup

from getReward import createExcel


def gteData(url, classAttr, exceName):
    # url = "http://www.most.gov.cn/cxfw/kjjlcx/kjjl2000/200802/t20080214_59081.htm"
    html_str = requests.get(url).content.decode("gbk", "replace")
    bs = BeautifulSoup(html_str, "html.parser")
    dict = {}
    for attr in classAttr:
        table = bs.find(name="table", attrs={"class": attr})
        tr = table.find_all(name="tr")
        father = []
        for obj in tr:
            td = obj.find_all(name="td")
            # print(p)
            son = []
            str = ""
            for obj in td:
                if obj.text.startswith("二等奖"):
                    dict.update({"一等奖": father})
                    father = []
                    son = []
                    continue
                else:
                    # son.append(obj.text)
                    p = obj.find_all(name="p")
                    if  len(p) > 1:
                        for pObj in p:
                            son.append(pObj.text)
                    else:
                        son.append(obj.text)
            father.append(son)
        dict.update({"二等奖": father})
    createExcel.create(exceName, **dict)


url = "http://www.most.gov.cn/cxfw/kjjlcx/kjjl2001/200802/t20080214_59030.htm"
# 2001年 一等奖二等奖在一个表格
classAttr = ['MsoNormalTable']
exceName = "2001年度国家科学技术进步奖目录"
gteData(url, classAttr, exceName)

def run():
    url = "http://www.most.gov.cn/cxfw/kjjlcx/kjjl2001/200802/t20080214_59030.htm"
    # 2001年 一等奖二等奖在一个表格
    classAttr = ['MsoNormalTable']
    exceName = "2001年度国家科学技术进步奖目录"
    gteData(url, classAttr, exceName)