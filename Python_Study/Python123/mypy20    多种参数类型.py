#位置参数
def test01(a,b,c,d):
    print(a,b,c,d)
test01(6,7,8,9)
#如果  test01(1,2)  就会报错，位置参数不匹配


#默认值参数
def test02(a,b,c=666,d=777):    #默认值参数咋普通参数后面
    print(a,b,c,d)
test02(1,2)


#命名参数
def test03(a,b,c,d):
    print(a,b,c,d)
test03(d=111,b=222,c=555,a=666)     #根据命名调整参数位置


#可变参数     一个*号，将多个参数收集到一个元组中；多个*号，将多个参数收集到字典中
def test04(a,b,c,*d):
    print(a,b,c,d)
test04(1,2,3,4,5,6,7,8,[9,10])


def test05(a,b,c,**d):
    print(a,b,c,d)
test05(1,2,3,name='wbx',bobby='basketball')


#强制命名参数     *号在前，后面的普通参数需强制命名
def test06(*a,c=8):
    print(a,c)
test06(1,2,3,4,5,6,c=888)
