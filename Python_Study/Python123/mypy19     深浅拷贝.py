import copy
#浅拷贝----不拷贝子对象的全部内容，只拷贝引用，对子对象的修改影响源对象
a=[1,2,3,[666,777]]
b=copy.copy(a)
print(a)
print(b)
b.append(4)
b[3].append(888)
print('浅拷贝.......')
print(a)
print(b)


print('_____________________________________________')
#深拷贝---拷贝子对象的全部内容，对子对象的修改不影响源对象
a=[1,2,3,[666,777]]
b=copy.deepcopy(a)
b.append(4)
b[3].append(888)
print('深拷贝.........')
print(a)
print(b)

