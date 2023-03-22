#测试旋转结构的嵌套
score=int(input('请输入分数0—100的分数:'))
if score<=0 or score>=100:
    print(int(input('分数不能小于0或大于100，再次输入分数：')))
    if score>90:
        grate='A'
    elif score>80:
        grate='B'
    elif score>70:
        grate='C'
    elif score>60:
        grate='D'
    else:
        grate='E'
    print('分数：{0},等级{1}'.format(score,grate))
    #注意缩进（从属关系，如果print放在grate下面，则如果输入一个>60的数，就不会打印
else:
    if score>90:
        grate='A'
    elif score>80:
        grate='B'
    elif score>70:
        grate='C'
    elif score>60:
        grate='D'
    else:
        grate='E'
    print('分数：{0},等级{1}'.format(score,grate))

    #0000000000000000000000000000000000000000000000000
    #简便算法
degree='ABCDE'
score=int(input('请输入你的分数：'))
num=score//10
if num<6:
    num=5

print('分数是{0}'.format(degree[9-num]))
