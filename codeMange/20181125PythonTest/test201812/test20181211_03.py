class Father:
    def run(self):
        print("跑的很快")

    def cook(self):
        print("不会做饭")

class Mother:
    def run(self):
        print("跑的很慢")

    def cook(self):
        print("会做饭")


class Son(Father, Mother):
    pass

son =Son()
son.run()
son.cook()
# (<class '__main__.Son'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>)
# 从左到右执行顺序
print(Son.__mro__)
print(dir(Son))
print(dir(Mother))