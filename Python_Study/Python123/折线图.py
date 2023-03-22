import turtle
import math
'''定义多个点的坐标
刚开始记得penup'''
x1,y1=150,150
x2,y2=-150,150
x3,y3=-150,-150
x4,y4=150,-150

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x4,y4)
distance=math.sqrt((x1-x4)**2+(y1-y4)**2)
turtle.write(distance)
