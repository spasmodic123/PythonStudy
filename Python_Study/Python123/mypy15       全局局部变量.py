#测试全局和局部的变量
a=9    #全局变量，整个过程永久使用
print(a)

def test01():
    b=8     #局部变量，用完就没
    print(b*8)
#在这一行print(b)会报错，显示b未被定义
    global a    #更改全局变量的方式
    a=100
    print(a)
    print(locals())#打印函数中的局部变量
    print(globals())#打印函数中的全局变量

test01()

