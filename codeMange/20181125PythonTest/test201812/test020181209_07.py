def demo1(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)
    print("*" * 100)


# 多值和缺省不一样
# demo1(2,name = 1)
# # # demo("小妹")
# # # demo("小妹","xiao","mei","xiaomei")
# # # # demo("小妹","xiao","mei","xiaomei",name="xiaomei",)
# # # demo(0,(1,2,3),{"name":"xiaomei"})


def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


demo(1, 2, 3, 4, 5, name="小米", old=19)
demo(1, 2, name="小米")
