#同心圆
import turtle
a=turtle
a.width(5)
a.speed(50)
color=('red','orange','yellow','green','blue','cyan','purple')




for x in range(30):
    a.color(color[x%7])
    a.circle(50+x*20)
    a.penup()
    a.goto(0,-20-20*x)
    a.pendown()

#棋盘
a.color('black')
for i in range(18):
    a.penup()
    a.goto(-200,-25*i)
    a.pendown()
    a.goto(200,-25*i)

for j in range(17):
    a.penup()
    a.goto(-200+25*j,0)
    a.pendown()
    a.goto(-200+25*j,-400)

a.done()

