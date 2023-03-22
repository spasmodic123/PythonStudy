import time
# 开始时间
time01=time.time()
a='i love you'
for i in range(1000000):
    a+='i love uou'
#结束时间
time02=time.time()
print("算了多久呢:"+str(time01-time02))


#二次测试，使用join而不是+   join用于字符串之间 是连接  qppend用于列表  是添加
#开始时间
a=["i love you"]
time03=time.time()
for i in range(1000000):
    a.append("i love you")
time04=time.time()
print("算了多久呢:"+str(time03-time04))
