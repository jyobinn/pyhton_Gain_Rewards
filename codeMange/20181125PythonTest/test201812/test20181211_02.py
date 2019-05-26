class Father:
    def run(self):
        print("跑的很快")


class Mother:
    def cook(self):
        print("会做饭")


class Son(Father, Mother):
    pass

son =Son()
son.run()
son.cook()