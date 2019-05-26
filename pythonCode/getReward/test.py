from urllib import parse

import requests
from bs4 import BeautifulSoup

from getReward import createExcel

# url = "http://www.most.gov.cn/cxfw/kjjlcx/kjjl2000/200802/t20080214_59081.htm"
# html_str = requests.get(url).content.decode("gbk", "ignore")
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

def gteData(url,classAttr,exceName):
    # url = "http://www.most.gov.cn/cxfw/kjjlcx/kjjl2000/200802/t20080214_59081.htm"
    html_str = requests.get(url).content.decode("gbk", "ignore")
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
                son.append(obj.text)
            father.append(son)
        dict.update({attr:father})
    createExcel.create(exceName, **dict)


url = "http://www.most.gov.cn/cxfw/kjjlcx/kjjl2000/200802/t20080214_59081.htm"
classAttr = ['MsoTableGrid','MsoNormalTable']
exceName ="2000年度国家科学技术进步奖目录"
gteData(url,classAttr,exceName)