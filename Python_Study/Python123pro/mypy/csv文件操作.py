import csv
with open(r"C:\pythonProject1\date2.csv",'r')as f:
    a=csv.reader(f)
    print(list(a))
    f.seek(1)#print之后,指针已经移动到最后,不能再继续for循环,需要重置指针
    for row in a:
        print(row)


with open(r"C:\pythonProject1\date2.csv",'a',newline='') as g:#newline防止出现空行
    xie=csv.writer(g)
    xie.writerow(['4','wuboxiong','www.handdome.com','666'])