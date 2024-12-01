a = 1, 2, 3, 4, 5
b = 1,2
print(f"type(a)={type(a)}, type(b)={type(b)}")
print(a)
print(b == (1,2))
#对a，b进行了隐式打包成元组

a = {}
a[1] = 2
a[1,2] = 1#在索引值中自动隐式打包成元组，因为元组是不可变类型，可以当作字典的键
print(a)
print(a[1,2])

a = [[1,2,3], [1,2,3]]
print(a[1][2])
print(a[1,2])#列表的索引值不能是元组
