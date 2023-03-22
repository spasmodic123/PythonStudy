class Person:
    def work(self):
        print('努力工作')

def play_game(x):     #要有一个参数，因为后面添加参数时,Person是有一个参数的，所以添加的方法也要有一个参数
    print('{0}玩minecraft，玩APEX'.format(x))

def work2(x):        #也要有一个参数
    print('好好学习，努力工作')

Person.play=play_game     #添加方法
Person.work=work2         #修改方法
a=Person()
a.work()
a.play()
