#嵌套函数，在函数里面定义函数
def print_name(isChinese,name,family_name):
    if isChinese:
        print(family_name,name)
    else:
        print(name,family_name)
print_name(True,'boxiong','wu')   # 正常写法

def PrintName(isChinese,name,family_name):
    def inner_print(a,b):
        print(a,b)
    if isChinese:
        inner_print(family_name,name)
    else:
        inner_print(name,family_name)

PrintName(True,'mo','wanling')   #只是了解嵌套函数，正常情况那种好用那种，这里显然上面的正常写法好