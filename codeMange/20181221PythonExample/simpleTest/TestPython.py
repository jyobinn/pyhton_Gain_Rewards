import requests
import re
from bs4 import BeautifulSoup


def getUrl(url):
    i = 0
    res = requests.get(url)
    bs = BeautifulSoup(res.text, "html.parser")
    for item in bs.find_all("a", href=re.compile('_xingzhengquhua')):
        print(item.get_text(), end="")
        i = i + 1
        if i % 2 == 0:
            print()
            # print("url" + item["href"])
            # url[0:-1] + item["href"]
            newUrl = url[0:-1] + item["href"]
            getUrl(newUrl)
        else:
            print("-" * 10, end="")


url = "https://xingzhengquhua.51240.com/"

getUrl(url)
