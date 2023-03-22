#计算尽量往外放，别放循环里边
import time
start1=time.time()
for a in range(10000):
    result = []
    for b in range(100000):
        result.append(a*1000+b*10000)
'''如果不把a*1000换成c单独列出来，就会多出来10000次无效运算，
因为每一次a的循环十万次，a*10000的值一样的，放在b循环里面就很多余
如果单独提出来，就减少很多次运算，也不改变结果'''
end1=time.time()
print('运算时间：',end1-start1)

start2=time.time()
for a in range(10000):
    result = []
    c=a*1000
    for b in range(100000):
        result.append(c+b*10000)
end2=time.time()
print('简化运算时间：',end2-start2)

#普通运算101秒，简化88秒