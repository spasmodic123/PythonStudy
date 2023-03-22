#break语句
while True:#True记得大写
    a=input('输入q或Q结束进程：')
    if a=='q' or a=='Q':    #记得双等于号,记得在q和加引号
        print(a)
        print('循环终止')
        break
    else:
        print(a)

print('---------------------------------------------------')
#continue语句
#输入每个员工的工资，计算平均
membersnumber=0
salarysum=0
salarys=[]
salaryave=0
while True:
    a=(input('请输入员工薪资；（按q或Q结束）'))
    if a=='q' or a=='Q':
        print('输入完成')
        break
    elif float(a)<0:
        continue
    else:
        membersnumber+=1
        salarysum+=float(a)
        salarys.append(float(a))
        salaryave=salarysum/membersnumber

print('总工资',salarysum)
print('人数',membersnumber)
print('平均',salaryave)
print(salarys)
