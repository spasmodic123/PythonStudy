import copy

class MobilePhone():
    def __init__(self,cpu,gpu,screen):
        self.cpu=cpu
        self.gpu=gpu
        self.screen=screen

class Cpu:
    def calculate(self):
        print('天玑8100',self)

class Gpu:
    def xuanran(self):
        print('rtx3060',self)

class Screen:
    def show(self):
        print('曲面屏',self)


a1=MobilePhone(Cpu(),Gpu(),Screen())      #这也是一个组合，将类Cpu，Gpu，Screen放到类MobilePhone中，拥有其他类的属性

#浅
print('测试浅拷贝.....')
a2=copy.copy(a1)
print(a1,a1.cpu,a1.gpu,a1.screen)
print(a2,a2.cpu,a2.gpu,a2.screen)    #浅拷贝，a1 a2相同，但里面的cpu。gpu，screen也相同


#深
print('测试深拷贝...')
a3=copy.deepcopy(a1)
print(a1,a1.cpu,a1.gpu,a1.screen)
print(a3,a3.cpu,a3.gpu,a3.screen)     #深拷贝，全部地址不一样，子对象也全部复制

