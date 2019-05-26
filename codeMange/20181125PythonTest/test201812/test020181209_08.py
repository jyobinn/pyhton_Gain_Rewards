def addSum(*args):
    """
    不管传入多少个，直接返回合计
    :param args: 参数个数不定
    :return: 合计
    """
    sum = 0
    for i in args:
        sum += i
    print(sum)
    return sum

addSum(1)
addSum(1,2)
addSum(1,2,3)
