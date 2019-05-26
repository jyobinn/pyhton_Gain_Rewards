class Test:
    # 类属性
    count = 0

    def __init__(self, name):
        self.name = name
        Test.count += 1

test =Test("test1")
# 类属性访问建议类名.属性
print(Test.count)
# 类属性访问不建议对象.属性
print(test.count)
print(test.name)
# print(Test.name)
test1 =Test("test12")
test2 =Test("test13")
test3 =Test("test14")
# 类属性访问建议类名.属性
print(Test.count)
# 类属性访问不建议对象.属性
print(test.count)
# test.count = 999
Test.count = 1458
# 类属性访问建议类名.属性
print(Test.count)
# 类属性访问不建议对象.属性
print(test.count)