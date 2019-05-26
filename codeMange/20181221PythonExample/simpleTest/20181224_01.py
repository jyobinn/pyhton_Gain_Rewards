from bs4 import BeautifulSoup

file = open('./a.html', 'rb')
html = file.read()
bs = BeautifulSoup(html,"html.parser")

# 获取所有的a标签，并遍历打印a标签的文本值
for item in bs.find_all("a"):
    print(item)
    print(item["href"])
    print(item["name"])
    print(item.get_text())