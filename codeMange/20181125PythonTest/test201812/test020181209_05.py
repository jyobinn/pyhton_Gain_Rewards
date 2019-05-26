str = [1, 2, 3]


def add(str):
    str.append(4)
    print(str)
    return str


def add2(str):
    str = [10, 11]
    print(str)
    return str


print(str)
add(str)
print(str)
add2(str)
print(str)
