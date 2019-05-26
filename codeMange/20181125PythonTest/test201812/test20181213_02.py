
try:
    str = int(input("请输入整数"))
    print(1000 / str)
except ZeroDivisionError:
    print("除以0的异常")

except Exception as result:
    print("不明问题 %s" % result)
else:
    print("前面没有问题")
finally:
    print("程序运行结束")
