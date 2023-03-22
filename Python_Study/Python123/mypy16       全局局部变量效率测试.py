import math
import time

def test01():
    start=time.time()
    for x in range(10000000):
        math.sqrt(90)  #全局变量
    end=time.time()
    print('耗时{0}'.format(end-start))

def test02():
    start=time.time()
    b=math.sqrt     #在函数里面创建了一个局部变量
    for x in range(10000000):
        b(90)   #在循环中，调用局部变量远快于全局
    end=time.time()
    print('耗时{0}'.format(end-start))

test01()
test02()