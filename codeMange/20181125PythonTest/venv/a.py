#第一种方法
import urllib  #将urllib2库引用进来
response=urllib.request("http://www.baidu.com") #调用库中的方法，将请求回应封装到response对象中
html=response.read() #调用response对象的read（）方法，将回应字符串赋给hhtml变量
print(html)  #打印出来