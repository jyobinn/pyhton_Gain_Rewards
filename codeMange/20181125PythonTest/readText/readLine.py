file = open("a.txt")
fileCopy = open("fileCopy.txt", "w")
while True:
    text = file.readline()
    if not text:
        break
    print(text)
    fileCopy.write(text)

file.close()
fileCopy.close()
