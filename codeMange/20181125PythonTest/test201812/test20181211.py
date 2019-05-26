class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


animal = Animal()
animal.run()


class Dog(Animal):

    def shut(self):
        print("汪汪汪")


dog = Dog()
dog.run()
dog.shut()


class SuperDog(Dog):

    def fly(self):
        print("会飞")

    def shut(self):
        super(SuperDog, self).shut()
        print("会说话")
        print("^&^&&^^&")


superDog = SuperDog()
superDog.eat()

superDog.fly()
print("*" * 100)
superDog.shut()
