class Music(object):
    singleton = None

    def __new__(cls, *args, **kwargs):
        if cls.singleton is None:
            # 为对象分配空间
            print("分配空间")
            cls.singleton = super(Music, cls).__new__(cls)
        # 返回对象引用
        return cls.singleton

    def __init__(self):
        print("初始化")

"""
单例模式。内存只有一份，即永远只存在一个对象在内存空间中
"""
music = Music()
music1 = Music()
print(music)
print(music1)
