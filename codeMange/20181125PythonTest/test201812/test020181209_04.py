a = 10

def add():
    # 全局变量
    global a
    a = 99
    print("add现在的a是%d" %(a,))
def add2():
    print("add2现在的a是%d" %(a,))

add()
add2()