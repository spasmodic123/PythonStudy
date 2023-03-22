#嵌套基础
for a in range(6):
    for b in range(6):
        print(a,end='\t')#如果print（a），第一行000000，打印的是a，b是次数：如果print（b），第一行012345，打印的是b，a是第几组
    print()

print('@@@@@@@@@@@@@@@@@@@@@@@@@@')
#九九乘法表
for a in range(1,10):
    for b in range(1,a+1):
        print('{0}*{1}={2}'.format(a,b,a*b),end='\t')
    print()

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#表格，与if结合一下
r1=dict(name='wuboxiong',address="广东",hobby='playing basketball',salary=200000)
r2=dict(name='梁铉',address="广西",hobby='playing pingpong',salary=300000)
r3=dict(name='lincangweei',address="广宁",hobby='打嘴炮',salary=400000)
tb=[r1,r2,r3]
for x in tb:
    if x.get('salary')>250000:
        print(x)
