#不可变对象的传递
a=111

def test01(x):
    print(x)
    print(id(x))         #传进x的地址
    x=x*6                #x为不可变对象，创建新的对象
    print(x)
    print(id(x))         #x的地址已经改变

test01(a)