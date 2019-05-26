def getNum(num):
    print(num)
    if num == 1:
        return 1
    # print(num)
    # temp =
    return num + getNum(num - 1)


print(getNum(100))
