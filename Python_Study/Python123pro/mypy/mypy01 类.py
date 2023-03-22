class GoodStudents:    #类命名首字母大写，多个单词驼峰原则
    def __init__(self,name,score):    #self必须是第一个参数,表示创建的实例本身,__init__函数初始化,表示创建这个 实例 有什么属性
        self.name=name
        self.score=score

    def say_score(self):    #self必须位于第一个参数
        print( '名字：{0},分数：{1}'.format(self.name,self.score))
        print("%s: %s"% (self.name,self.score) )

s1=GoodStudents('wuboxiong',18)      #通过类名（）调用构造函数
s1.say_score()