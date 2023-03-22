#测试递归函数，在函数里面调用函数。遵循先进后出，后进先出！
def test01():
    print('test01')
    test02()
    print('再打印这个')

def test02():
    print('test02')
    print('先打印这个')

test01()
print('___________________________________')


def test03(n):
    if n==0:
        print('结束')
    else:
        print('test03',n)
        test03(n-1)
    print(n)      #输入n后，执行test（n-1）后，不会立刻打印n，而是先存起来，因为先进后出，后进先出。test（6）最先输入，print（6）最后输出
test03(6)