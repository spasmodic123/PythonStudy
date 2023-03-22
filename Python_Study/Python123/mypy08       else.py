#for循环中的 else 语句, 结合continue和break
salarySUM=0
salarys=[]
for a in range(4):
    a=input('请输入一共四名员工的工资：（按q或Q结束进程）')
    if a=='q' or a=='Q':
        print('未全部输入四名员工工资，提前结束')
        break
    elif float(a)<=0:
        continue
    salarySUM+=float(a)
    salarys.append(a)

print('成功输入四名员工的工资', "平均工资：", salarySUM / 4)
print('录入薪资：',salarys)


