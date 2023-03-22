#测试LEGB规则
str='global str'   #再寻找外部的全局变量
def outer():
    str='outer str'   #再寻找嵌套
    def inner():
        str='inner str'    #名称都为str，先寻找函数或者类的方法内部
        print(str)
    inner()
outer()