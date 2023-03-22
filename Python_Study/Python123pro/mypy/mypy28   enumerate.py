a=["静夜思","I see a silver light","床前明月光，"]
print(a)
b=enumerate(a)#b是枚举对象,需要手动转化list
print(list(b))

c=[content + ' #' +str(index) for index,content in enumerate(a)]#结合推导式
print(c)
