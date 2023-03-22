
d=(0,1,2,3,4,5,6,7,8,9,6666)   #元组
for x in d:
    print(x,end='\n')

a={'name':'wuboxiong','weigh':62,'high':.7,'hobby':'listening music'}
for x in a.values():
    print(x)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


for x in range(12):
    print(x)

#计算1-100累加和
sum_all=0
sum_odd=0
sum_even=0
for x in range(101):
    sum_all+=x
    if x%2==1:   #用双等于号而不是单等于号
        sum_odd+=x
    else:
        sum_even+=x
print(sum_all)
print(sum_odd)
print(sum_even)
print('总和是{0}，奇数和是{1}，偶数和是{2}'.format(sum_all,sum_odd,sum_even),end='\n')
print('总和是{zonghe},奇数是{jishu},偶数和是{oushu}'.format(zonghe=sum_all,jishu=sum_odd,oushu=sum_even))


n=5
all=1
while n>0:
    all*=n
    n-=1
print(all)