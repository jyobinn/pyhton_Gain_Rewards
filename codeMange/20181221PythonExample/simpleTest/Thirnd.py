# _*_ coding:utf-8 _*_
import urllib,urllib.request

from pip._vendor.distlib.compat import raw_input

url = 'http://www.baidu.com/s'
headers = {'UserAgent':'Mozilla'}
keyword = raw_input('请输入关键字:')
wd = urllib.parse.urlencode({'wd':keyword})
fullurl = url + '?' + wd
print(fullurl)
request = urllib.request.Request(fullurl,headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode("utf-8"))
# wd=%E7%BE%8E%E5%A5%B3&rsv_spt=1&rsv_iqid=0xd8899c6e000412a5&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&oq=python%2526lt%253B%2520%25E4%25BB%2580%25E4%25B9%2588%25E4%25BB%25A3%25E6%259B%25BFurlencode&rsv_t=1bec72b%2FgmdPeFv%2FUR5CwW%2FSz0u5dJOJlg6X5XX7NTsevzn4EJhdvKbIF%2F2PBJXgIxuB&inputT=1137&rsv_pq=96aa4b2900036860&rsv_sug3=25&rsv_sug1=25&rsv_sug7=100&rsv_sug2=0&rsv_sug4=1137
# wd=%E7%BE%8E%E5%A5%B3