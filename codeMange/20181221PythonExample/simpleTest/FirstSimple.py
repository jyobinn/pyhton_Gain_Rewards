# _*_ coding:utf-8 _*_
import urllib.request

# User-Agent是爬虫与反爬虫的第一步
ua_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'}
# 通过urllib2.Request()方法构造一个请求对象
request = urllib.request.Request('http://www.baidu.com/',headers=ua_headers)

#向指定的url地址发送请求，并返回服务器响应的类文件对象
response = urllib.request.urlopen(request)

# 服务器返回的类文件对象支持python文件对象的操作方法
# read()方法就是读取文件里的全部内容，返回字符串
html = response.read()

# 返回HTTP的响应吗，成功返回200,4服务器页面出错，5服务器问题
print(response.getcode())     #200

# 返回数据的实际url,防止重定向
print(response.geturl())     #https://www.baidu.com/

# 返回服务器响应的HTTP报头
print(response.info())

# print html