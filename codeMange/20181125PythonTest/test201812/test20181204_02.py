import keyword

print(keyword.kwlist)
singel_tuple = ()
print(type(singel_tuple))
tuple3 = (6)
print(type(tuple3))
tuple2 = (78,)
print(type(tuple2))

print("%s 的年龄是 %d 岁，身高是 %.2f 米" % ("jyo", 23, 1.74))
infor = ("jyo", 23, 1.74)
print("%s 的年龄是 %d 岁，身高是 %.2f 米" % infor)

# tuple 元祖
# list 列表
num_list = [1, 2, 3, 4]
print(type(num_list))
num_tuple = tuple(num_list)
print(type(num_tuple))
real_list = list(num_tuple)
print(type(real_list))

jyo = {
    "name": "王小明",
    "age": 18,
    "height": 1.56,
    "flag": True
}
print(jyo)
print(jyo["name"])
jyo["name"] = "张一帆"
jyo["simpleName"] = "zhang"
print(jyo)
bat = {
    "name": "Mr Sun",
    "lanuage": "En"
}
jyo.update(bat)
print(jyo)

for i in jyo:
    print("%s - %s" % (i, jyo[i]))

str = "asadsdadsad"
print(str.count("Sad"))
str = "asadsdadsadad231"
print(str.isalpha())
print(str.isalnum())
print("*"*10)
str = "sad_sad"
print(str.islower())
print(str.isupper())
str = "sad_sasadSSSd"
print(str.islower())
print(str.isupper())
str = "SAGHGSSh"
print(str.islower())
print(str.isupper())
str  = "PRTTT_TYTY_ASD"
print(str.replace("_"," "))
print(str.replace("_"," ").lower().title())
print(str.replace("_"," ").lower().title().replace(" ",""))
str = str.replace("_"," ").lower().title().replace(" ","")
str  = "PRTTT_TYTY_ASD"
print(str.title())
abc = str.title().split("_")
print("*"*100)
abc[0]=abc[0].lower()
print("".join(abc))
k="".join(abc)
print("".join(abc).upper())
print(abc)
str="asadad"
print(str.upper())
print(str)