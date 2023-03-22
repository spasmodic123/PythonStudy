#列表推导式
a=[]
for x in range(1,50):
    if x%3==0:
        a.append(x*2)
print(a)                  #普通

a=[x*2 for x in range(1,50) if x%3==0]
print(a)                  #推导式简便表达


for a in range(1,10):        #普通
    for b in range(1,10):
        hahaha = (a, b)
        print(hahaha,end='\t')
    print()#打印空白，起到换行作用

hahaha=[(a,b)for a in range(1,50) for b in range(1,50)]    #推导式表达
print(hahaha)

print('-------------------------------------------------------------')


#字典的推导式表达
my_text='i have fallen in love deeply with you since the first time i met you.And you are my sunshine'
letter_num={c:my_text.count(c)for c in my_text}
print(letter_num)

print('@@@@@@@@@@@@@@@@@@@@@@@@@22')

my_text='i have fallen in love deeply with you since the first time i met you.And you are my sunshine'
for a in my_text:
    print({a:my_text.count(a)})

#集合推导式
a={x for x in range(1,50)}
print(a)     #集合与字典差不都，集合只有键，没有值


#生成器（元组）推导式
gnt=(x for x in range(1,6))
print(tuple(gnt))
print(tuple(gnt))#生成器只能使用一次，第二次打印空白

gnt=(x for x in range(1,6))
for x in gnt:
    print(x,end='\t')
print(tuple(gnt))#循环一次后打印也是空白


