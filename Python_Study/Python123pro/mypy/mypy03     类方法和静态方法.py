#测试类方法和静态方法
class Students:
    school='肇庆一中'   #类属性

    def __init__(self,name,age):   #创建的实例对象有name,age两种属性
        self.name=name
        self.age=age


    @classmethod    #类方法
    def print_school(cls):
        print(cls.school)     #类方法操作类属性
        #print(self.name)      在类方法和静态方法中不能调用实例属性

    @ staticmethod    #静态方法
    def add(a,b):
        print('{0}+{1}={2}'.format(a,b,a+b))    #静态方法操作与类属性无关的对象
    add(20,30)

Students('WUBOXIONG',18)
Students.print_school()
Students.add(66,77)
