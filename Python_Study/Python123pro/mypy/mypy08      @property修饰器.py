#将方法调用变为属性调用
class Person:
    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary


    @property
    def salary(self):
        return self.__salary

    @salary.setter      #这一步setter装饰器，可以在下面22行修改salary属性
    def set_salary(self,x):
        if 1000<x<50000:
            self.__salary=x
        else:
            print('输入错误，请输入1000--50000的工资')

a=Person('wbx',100000)

print(a.salary)       #用了@property之后，变成了引用属性，不需要a.salary(),不需要括号
a.set_salary=6666
print(a.salary)