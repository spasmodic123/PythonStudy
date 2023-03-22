from functools import reduce

#重写int()函数
digit={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

a='123456'
def str_to_int(s):
    def add(x,y):
        return x*10+y
    def char_to_int(s):
        return digit[s]
    return reduce(add,map(char_to_int,s))   #先利用map函数遍历s字符串,将每一个字符转换成int,在利用reduce函数累加计算
print(str_to_int('123456'))


def cifang(x):
     return x**3

b=[1,2,3,4,5,6,7,8,9]
print( list(map(cifang,b)) )   #因为map函数返回iterator,迭代器,不能直接打印,要用list函数转换
