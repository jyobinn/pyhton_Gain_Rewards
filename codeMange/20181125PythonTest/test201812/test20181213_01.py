# str = int(input("请输入整数"))
# print(1000/str)
# 输入0报 ZeroDivisionError
# 输入字符串报 ValueError
try:
    str = int(input("请输入整数"))
    print(1000 / str)
except ZeroDivisionError:
    print("除以0的异常")
# except ValueError:
#     print("字符串转整数失败")
except Exception as result:
    print("不明问题 %s" % result)
