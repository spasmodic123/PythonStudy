#函数的定义和调用
def fun01():
    a=input('请输入你儿子的名字：')
    if a=='岑百森' or a== 'cenbaisen':
        print('yes')
    else:
        print('no')

fun01()

#形参和实参
def contrast(a,b,c):
    if a>b and a>c:
        print(a,'最大值')
    elif b>a and b>c:
        print(b,'最大值')
    else:
        print(c,'最大值')

contrast(10,20,30)

def print_star(x):
    '''打印 x个数量的星号'''     #函数注释
    print('*'*x)

print_star(10)

help(print_star.__doc__)