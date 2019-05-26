list =[1,2,3]
print(id(list))
list =[4,5,6]
print(id(list))
list.extend([8,9])
print(list)
print(id(list))