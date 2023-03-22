class Person:
    def __init__(self,name):
        self.name=name

    def __add__(self, other):      #重载加法方法，如果不重载，不支持类的相加，unsupported operand type(s) for +: 'Person' and 'Person'
        if isinstance(other,Person):
            return '{0}---{1}'.format(other.name,self.name)
        else:
            print('不是同类，不能相加')

    def __mul__(self, other):       #重载乘法方法，否则 unsupported operand type(s) for *: 'Person' and 'int'
        if isinstance(other,int):
            return self.name*other


class Person2:
    def __init__(self,name):
        self.name=name

p1=Person('wuboxiong')
p2=Person('zhangjiewei')
p3=Person2('岑百森')
p4=Person('jiangjunhua')

print(p1+p2)   #zhangjiewei---wuboxiong
print(p1+p3)   #不是同类，不能相加
print(p4*9)