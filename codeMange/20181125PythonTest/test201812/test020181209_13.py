class Person:
    def __init__(self, self_name, self_weight):
        print("初始化姓名:%s 体重:%d" % (self_name, self_weight))
        self.name = self_name
        self.weight = self_weight

    def run(self):
        print("%s开始跑步" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s开始吃饭" % self.name)
        self.weight += 1

    def __str__(self):
        return "%s的体重%.2f" % (self.name, self.weight)

    def str(self):
        print("*"*100)
        return "%s的体重%.2f" % (self.name, self.weight)
person = Person("黑猫", 1.69)
person.run()
person.eat()
print(person)
print("@"*100)
person.str()
