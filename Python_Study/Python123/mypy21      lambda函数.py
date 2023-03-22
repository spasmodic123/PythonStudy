a=lambda a,b,c,d,e:a*b*c*d*e
print(a(1,2,3,4,5))

def test01(a,b,c,d,e):
    return a*b*c*d*e
print(test01(1,2,3,4,5))     #与上面的结果一致

print('//////////////////////////')

b=[lambda a,b,c,d:a+b+c+d,lambda e,f:e**f]   #函数也是对象
print(b[0](6,7,8,9))
print(b[1](9,2))

print('//////////////////////////')

def myfunc(n):
    return lambda a:a*n

mydouble=myfunc(2)
mytriple=myfunc(3)
print('两倍:',mydouble(11))
print('三倍:',mytriple(11))


