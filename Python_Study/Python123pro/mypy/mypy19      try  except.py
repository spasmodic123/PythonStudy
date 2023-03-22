#如果有异常，跳过异常之后的语句，执行except
'''循环输入多个数字知道出现666'''
while True:
    '''如果输入非数字，跳过，循环继续'''
    try:
        a=int(input("请输入一个数字:"))
        if a==666:
            print('程序结束')
            break
        else:
            print('continue')

    except BaseException as e:
        print(e)
        print('请输入数字，不是其他类型的数据')
