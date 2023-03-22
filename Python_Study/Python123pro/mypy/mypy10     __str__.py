class Person:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return  '我的名字是{0}'.format(self.name)

a=Person('wuboxiong')
print(a)          #如果不重写str，打印的是<__main__.Person object at 0x000002C1F88E7F10>