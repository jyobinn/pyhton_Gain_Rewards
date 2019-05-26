def demo():
    str = input("请输入一个字符")
    if (len(str) > 1):
        print("输入出错")
        ex = Exception("麻烦您输入一个字符")
        raise ex
    else:
        print("你好厉害")

try:
    demo()
except Exception as  errorMsg:
    print("错误消息是 %s" % errorMsg)
