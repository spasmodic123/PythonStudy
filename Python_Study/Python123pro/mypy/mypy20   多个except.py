try:
    a=float(input('输入一个数字'))
    b=float(input('再次输入一个数字'))
    c=a/b/d
    print(c)
except ZeroDivisionError:
    print('0不能作除数')
except NameError:
    print('变量不存在')
except ValueError:
    print('输入的非数字')
except BaseException:
    print('程序结束')