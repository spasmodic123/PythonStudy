#多分支结构
name=input('请输入名字:')
print(name if len(name)<10 else '名字太长')

print('0000000000000000000000000000')
x=int(input('请输入横坐标x：'))
y=int(input('请输入纵坐标y：'))
if(x==0 and y==0): print('原点')
elif(x==0):print('位于y轴')
elif(y==0):print('位于x轴')
elif(x>0 and y>0):print('第一象限')
elif(x<0 and y>0):print ('第二象限')
elif(x<0 and y<0):print('第三象限')
else:print('第四象限')

print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
a=input('请输入身高：')
b=input('请输入体重：')
print('身高是{0}，体重是{1}'.format(a,b))
if float(b)/float(a)**2<18.5:
    print('偏瘦')
elif float(b)/float(a)**2<=23.9:
    print('标准')
elif float(b)/float(a)**2<=27.9:
    print('偏胖')
else:
    print('肥胖')