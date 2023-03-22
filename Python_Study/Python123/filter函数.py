#filter函数与map函数类似,接受函数和一个iterable,然后根据返回值是True还是False决定保留还是丢弃该元素
import math
import setuptools.installer


def is_odd(x):    #判断偶数,并且丢弃奇数
    return x%2==0

a=[1,2,3,4,5,6,7,8,9,10]
print( list (filter(is_odd,a)) )
#结果   [2, 4, 6, 8, 10]



def not_empty(s):  #删除空格和none
    return s and s.strip()

b=['1',None,'','9','78','254','1234','556','ABC','','']
print( list(filter(not_empty,b))  )
#结果   ['1', '9', '78', '254', '1234', '556', 'ABC']


def sqr_is_int(x):
    return math.sqrt(x)%1==0

print( list (filter(sqr_is_int,range(100))) )
