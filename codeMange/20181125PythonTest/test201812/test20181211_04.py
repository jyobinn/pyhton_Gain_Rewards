class Dog:
    def __init__(self, name):
        self.name = name

    def play(self):
        print("%s在汪汪叫" % self.name)

    def playFather(self):
        print("%s在汪汪叫12345" % self.name)


class SuperDog(Dog):

    def play(self):
        print("%s在说话" % self.name)

    def playSon(self):
        print("%s在说话" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def playWithDog(self, dog):
        print("*" * 100)
        print("%s 在和 %s" % (self.name, dog.name))
        dog.play()
        dog.playFather()
        # dog.playSon()
        print("*" * 100)


dog = Dog("普通狗")
dog2 = Dog("普通狗")
dog.play()
superDog = SuperDog("超级狗")
superDog.play()
personA = Person("小明")
personA.playWithDog(dog)
personA.playWithDog(superDog)
print(Dog)
