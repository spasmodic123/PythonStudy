class A:
    def __init__(self,a):
        self.shuxing=a

    def say(self):
        print('aaaaaaaaaaaaaaaa')

class B:
    def say(self):
        print('bbbbbbbbbbbbbbb')

class C:
    def say(self):
        print('cccccccccccccc')

class D(B,C,A):
    pass

x=D(111)
x.say()     #解释器从左到右寻找相同名字的say(),D(B,C,A):

abc=D('属性')
print(abc.__dict__)     #对象的属性字典
print(abc.__class__)    #对象所属的类
print(D.__bases__)      #类的基类元组（多继承）
print(D.__mro__)        #类的层次结构
print(A.__subclasses__())    #子类列表

