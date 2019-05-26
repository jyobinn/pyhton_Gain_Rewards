from time import sleep

import requests
from bs4 import BeautifulSoup

from demo.Place import Place


def getBytesByURL(url):
    """
    查询所有需要的td的列表
    :param url: 请求地址
    :return:
    """
    print(requests.get(url).content)
    html_str = requests.get(url).content.decode()
    bs = BeautifulSoup(html_str, "html.parser")
    tdList = bs.find_all("td", bgcolor="#FFFFFF")
    return filterList(tdList)


def filterList(list):
    """
    去除不符合要求的列表
    :param list: td的列表
    :return:
    """
    if list == None or len(list) == 0:
        return []
    newList = []
    for obj in list:
        if obj.get("colspan") == None:
            newList.append(obj)
    return newList


def getPlaceList(tdList):
    """
    dom 转列表对象
    :param tdList:
    :return:地区列表
    """
    i = 0
    realList = []
    place = Place()
    for td in tdList:
        i += 1
        if i % 3 == 1:
            # print(td)
            # print(td.text)
            # 名字
            place.nameCn = td.text
        if i % 3 == 2:
            # print(td)
            # print(td.text)
            # 编码
            place.code = td.text
            place.url = "https://xingzhengquhua.51240.com/" + td.text + "__xingzhengquhua/"
        if i % 3 == 0:
            realList.append(place)
            place = Place()
    return realList


"""
这个是测试方法
"""
if __name__ == '__main__':
    # url = "https://xingzhengquhua.51240.com/110101001000__xingzhengquhua/"
    # url = "https://xingzhengquhua.51240.com"
    i = 0
    url = "https://xingzhengquhua.51240.com/"
    i+=1
    print(i)
    list_1st = getPlaceList(getBytesByURL(url))
    sleep(5)
    for obj_1st in list_1st:
        i += 1
        print(i)
        obj_1st.list = getPlaceList(getBytesByURL(obj_1st.url))
        sleep(5)
        for obj_2st in obj_1st.list:
            i += 1
            print(i)
            obj_2st.list = getPlaceList(getBytesByURL(obj_2st.url))
            sleep(5)

    for obj_1st in list_1st:
        print(obj_1st.nameCn)
        for obj_2st in obj_1st.list:
            print("\t" + obj_2st.nameCn)
            for obj_3st in obj_2st.list:
                print("\t\t" + obj_3st.nameCn)