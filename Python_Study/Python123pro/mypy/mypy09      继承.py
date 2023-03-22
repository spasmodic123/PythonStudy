class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age   #私有方法

    def test01(self):
        print('hahahahahahah')


class Student(Person):       #Student-->Person-->Object继承
    def __init__(self,name,age,score,rank):
        Person.__init__(self,name,age)     #调用父类的方法
        self.score=score
        self.rank=rank

    def introduce(self):
        print('{0},{1}岁，分数{2}，等级{3}'.format(self.name,self._Person__age,self.score,self.rank))


a=Student('吴博雄',18,149,'A')
a.test01()               #继承父类的test01
print(a._Person__age)     #调用父类的私有方法依旧要用此格式
a.introduce()

