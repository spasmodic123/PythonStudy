class Danli:
    __obj=None            #私有类属性
    __init_flag = True    #创建一个私有的init初始化标记

    def __new__(cls, *args, **kwargs):
        if cls.__obj==None:
            cls.__obj=object.__new__(cls)

        return cls.__obj

    def __init__(self,name):
        if Danli.__init_flag:
            print('init.....')
            self.name=name
        Danli.__init_flag=False     #执行一次之后就不会再次执行该初始话代码

a1=Danli('wuboxiong')
a2=Danli('zhangjiewei')
a3=Danli('cenbaisen')
print(a1)
print(a2)
print(a3)
