class Man:
    pass

class Chinese(Man):
    def eat(self):
        print('筷子')
class English(Man):
    def eat(self):
        print('刀叉')
class Indian(Man):
    def eat(self):
        print('徒手抓饭')
class Baby(Man):
    def eat(self):
        print('勺子')

def eat_method(x):
    if isinstance(x,Man):
        x.eat()
    else:
        print('未找到')

eat_method(Chinese())     #记得加括号，Chinese()
eat_method(English())
eat_method(Indian())
