# 不输入整数代码出错
# str = int(input("请输入整数"))
try:
    str = int(input("请输入整数"))
    # print(1000/str)
except:
    print("您输入的不是整数")