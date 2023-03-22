#测试return函数
def add(a,b):   #两个数相加
    return a+b      #return第一个功能，返回值
print(add(10,90))

def test01():
    print('hahahahahahah')
    print('我是靓仔'*6)
    return         #return第二个功能，结束函数，不会打印下面的123456789
    print('123456789')

test01()

def test02(a,b,c):
    return [a*10,b*10,c*10]     #返回多个值，利用列表，字典，元组，集合存起来
print(test02(7,8,9))
