class CountSalary:
    def __call__(self,salary):
        print('工资计算')
        monthsalary=salary
        yearsalary=salary*12
        daysalary=salary/22.5
        hoursalary=daysalary/11

        return dict(monthsalary=salary,yearsalary=yearsalary,daysalary=daysalary,hoursalary=hoursalary)

a=CountSalary()
print(a(100000))
#obj(),一个对象加括号，代表调用__call__的方法
