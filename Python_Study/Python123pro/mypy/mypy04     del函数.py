class person:
    def __del__(self):
        print('销毁程序{0}'.format(self))

p1=person()
p2=person()
p3=person()
del p3
print('程序结束')    #程序结束后，p1和p2引用次数为0，被自动删除
