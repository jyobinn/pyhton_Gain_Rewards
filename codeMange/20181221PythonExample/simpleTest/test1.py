import time

from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Chrome(r"C:\Users\jyo\AppData\Local\Programs\Python\Python37\Lib\chromedriver.exe")
url = 'https://xingzhengquhua.51240.com'
res = browser.get(url)
print(res)
# bs = BeautifulSoup(res.text, "html.parser")
# browser.quit()