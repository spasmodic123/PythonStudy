class Member:

    __university='中山大学'    #私有类属性

    def __init__(self,name,age):
        self.name=name
        self.__age=age      #私有属性

    def __test01(self):     #私有方法
        print('保持热爱，好好生活')
        print(Member.__university)

a=Member('wbx',18)

print(a.name)
#print(a.age)      age已变为私有属性,会报错
print(a._Member__age)    # 访问私有属性的方式，_类名__私有属性（方法）名
a._Member__test01()      #访问私有方法

print(a._Member__university)