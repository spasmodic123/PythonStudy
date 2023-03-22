class Students:

    company='微软'     #类属性
    member_number=0

    def __init__(self,name,occupation):    #实例属性
        self.name=name
        self.occupation=occupation
        Students.member_number+=1

    def say_occupation(self):      #实例方法
        print('我的公司是：',Students.company)
        print(self.name,'的职业是',self.occupation)
        print('{0} 的职业是{1}，在{2}公司工作'.format(self.name,self.occupation,Students.company))

z1=Students('chari pule','engineer')    #实例对象，z是实例对象，自动调用__init__方法
z1.say_occupation()

z2=Students('Bod','ceo')
z3=Students('mary','cfo')
print('创建了{0}个对象'.format(Students.member_number))