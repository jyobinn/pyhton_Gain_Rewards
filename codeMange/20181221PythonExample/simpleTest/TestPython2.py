import requests
import re
from bs4 import BeautifulSoup

url = "https://xingzhengquhua.51240.com/110000000000__xingzhengquhua/"
res = requests.get(url)
# print(res.text)

bs = BeautifulSoup(res.text, "html.parser")
i = 0
for item in bs.find_all("a", href=re.compile('_xingzhengquhua')):
    # print(item["href"])
    res = requests.get(url[0:-1]  + item["href"])
    # print(type(item["href"]))
    # print("*"*100)
    # print(len(url))
    # print(str(url).rsplit(3,-1))
    # print("https://xingzhengquhua.51240.com/110000000000__xingzhengquhua/")
    # print(url[0:-1] + item["href"])
    print(item["href"])
    # print(res.text)
    break
    # print(item.get_text(), end="")
    # i = i + 1
    # if i % 2 == 0:
    #     print()
    # else:
    #     print("-"*10, end="")
