class CarFactoty:
    def create_car(self,brand):
        if brand=='Rolls_royces':
            return Rolls_royce
        elif brand=='Lamborghini':
            return Lamborghini
        elif brand=='Ferrari':
            return Ferrari
        elif brand==Byd:
            return Byd
        else:
            print("没有此类型的车")

class Rolls_royce:

    __init_flag=True       #同时测试单例模式，创建标记
    obj=None

    def __new__(cls, *args, **kwargs):
        if Rolls_royce.obj==None:
            Rolls_royce.obj=object.__new__(cls)
        return Rolls_royce.obj

    def __init__(self,price,accelerate100,rank):
        if Rolls_royce.__init_flag:
            print('初始化中....')
        self.price=price
        self.__accelerate100=accelerate100     #私有实例属性
        self.rank=rank
        Rolls_royce.__init_flag=False

class Lamborghini:
    pass

class Ferrari:
    pass

class Byd:
    pass

a0=Rolls_royce('8000000','3s','SS')

factory=CarFactoty()
a1=factory.create_car('Rolls_royces')
a2=factory.create_car('Lamborghini')
a3=factory.create_car('Ferrari')
print(a2.__dict__)
print(a0._Rolls_royce__accelerate100)    #访问私有属性


a001=Rolls_royce(6000000,'2.5s','AA+')
a002=Rolls_royce(9000000,'2.1s','SSS')
a003=Rolls_royce(5000000,'4s','B')
print(a001)
print(a002)
print(a003)
'''创建多个相同的对象，但只初始化了一次'''

