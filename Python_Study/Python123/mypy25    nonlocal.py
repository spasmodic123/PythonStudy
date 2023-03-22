#声明外层的局部变量
b=888
def outer():
    a=111
    def inner():
        nonlocal a    #声明外部函数的局部变量,第六和第七行不能调换位置，声明之后才能使用
        print(a)
        a=222
        print(a)
        global b   #声明外内部的全局变量，也是声明后才能使用
        print(b)
        b=999
        print(b)
    inner()
outer()

