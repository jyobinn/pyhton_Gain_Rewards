class Music(object):

    def __new__(cls, *args, **kwargs):
        print("分配空间")
        # 为对象分配空间，返回对象引用
        return super(Music, cls).__new__(cls)

    def __init__(self):
        print("初始化")

"""
内存开辟了多个
"""
music = Music()
music1 = Music()
print(music)
print(music1)
