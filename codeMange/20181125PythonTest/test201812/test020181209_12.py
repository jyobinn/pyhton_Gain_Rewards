class Cat:
    def __init__(self, self_name):
        print("初始化方法")
        self.name = self_name

    def drink(self):
        print("%s爱喝水" % self.name)

    def eat(self):
        print("小猫爱吃鱼")


tom = Cat("汤姆")
# tom.name = "汤姆"
tom.drink()
print(tom)
addr = id(tom)
print("%d" % addr)
print("%x" % addr)
