class A:
    def say(self):
        print('A',self)

class B(A):
    def say(self):
        #A.say(self)     与下一行作用一样
        super().say()
        print('B',self)
B().say()