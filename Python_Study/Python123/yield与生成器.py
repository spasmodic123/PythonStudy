g=(i for i in range(16))   #g是一个生成器
for i in g:
    print(i)

print('======================================')

def test01():
    print('step 1')
    yield 111
    print('step 2')
    yield 222
    print('step 3')
    yield 333

o=test01()
next(o)
next(o)
next(o)


def fab(x):
    n,a,b=0,0,1
    while n<x:
        yield b
        a,b=b,a+b
        n+=1
    return

z=fab(6)
for i in z:
    print(i,end=' ')
print('\n\n')


#定义函数


def triangles():
    L = [1]
    n=0
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]

sanjiao=triangles()
a=0
for i in sanjiao:
    print(i)
    a+=1
    if(a==10):
        break
