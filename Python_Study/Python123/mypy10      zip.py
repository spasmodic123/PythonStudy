#测试zip()的并行迭代
name=('wuboxiong','zhangjiewei','cenbaisen','zhuzhenyue')
hobby=('playing bsketball','打王者','看二次元')
address=('封开','德庆','江口')
occupation=('程序员','律师','物流管理员','篮球选手')

for a,b,c,d in zip(name,hobby,address,occupation):
    print('{0}--{1}--{2}--{3}'.format(a,b,c,d))
#并行迭代意思是把name，bobby，address，occupation四行并在一起输出，如每一行的第0个，每一行的第1个

print('___________________________________________________')
name=('wuboxiong','zhangjiewei','cenbaisen','zhuzhenyue')
hobby=('playing bsketball','打王者','看二次元')
address=('封开','德庆','江口')
occupation=('程序员','律师','物流管理员','篮球选手')
for i in range(3):
    print('{0}--{1}--{2}--{3}'.format(name[i],hobby[i],address[i],occupation[i]))
