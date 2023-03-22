class A:
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

x=D()
x.say()
print(D.mro())      #打印层次顺序