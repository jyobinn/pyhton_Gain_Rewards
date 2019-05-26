class Animal:
    def __init__(self, real_name):
        self.name = real_name
        self.__id = "动物"

    def run(self):
        print("%s会动,id是%s" % (self.name, self.__id))

    def __run(self):
        print("%s会动,id是%s" % (self.name, self.__id))


animal = Animal("Jyo")
# 在外界私有属性不能被访问
# print(animal.__id)
animal.run()
# 在外界私有方法不能被访问
# animal.__run()
# 伪私有 对象._类名__属性
print(animal._Animal__id)
# 伪私有 对象._类名__方法
animal._Animal__run()