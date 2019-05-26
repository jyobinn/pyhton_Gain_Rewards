def say():
    print("执行一次")



# __main__ 输出
print(__name__)
print("start")
say()

print("*"*100)
if __name__ == "__main__":
    print(__name__)
    print("start")
    say()