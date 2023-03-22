r1=dict(name='GTA5',rate='5star',company='roll star',price='198')
r2=dict(name='荒野大嫖客2',rate='5star',company='R星',price=124)
r3=dict(name='APEX',rate='6star',company='暴雪',price='free')#多个元素间记得用逗号隔开
#输入表格数据
tb=[r1,r2,r3]

#获得第三个游戏的价格
print(tb[2].get('price'),end='\n\n')

#获得全部数据
for i in range(3):
    print(tb[i].get('name'),tb[i].get('rate'),tb[i].get('company'),tb[i].get('price'))
    #不要吧.get的顿号写成逗号
      
