list = [0, 1, 2, 3, 4, 5, 6, 7]
for i in list:
    print(i)
else:
    print(999)

for i in list:
    print(i)
    if i == 3:
        break
else:
    # 循环体内部如果遇到break
    # else代码块不会被执行
    print(999)
