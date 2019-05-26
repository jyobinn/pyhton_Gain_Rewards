class Tools:
    count = 0
    __count = 0
    __defautName = "Tools"

    @classmethod
    def showTools(cls):
        print("实例化数量%d" % Tools.count)

    def __init__(self):
        Tools.count += 1

    @staticmethod
    def run():
        print("Tools is good")

    @staticmethod
    def run2(name):
        print("%s say Tools is good" % name)

    @staticmethod
    def run3(name):
        print("%s say Tools [%s] is good" % (name, Tools.__defautName))


Tools.run()
Tools.run2("ZXC")
Tools.run3("ASB")
print(Tools.count)
# print(Tools.__count)
tools1 = Tools()
tools1 = Tools()
tools1 = Tools()
Tools.showTools()
tools1.showTools()
