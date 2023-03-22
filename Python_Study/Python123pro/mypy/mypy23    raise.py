#定义一个异常,然后初始化
class AgeError(Exception):
    def __init__(self,ageinformation):
        Exception.__init__(self)
        self.ageinformation=ageinformation
    def __str__(self):   #打印异常信息时调用此方法
        return str(self.ageinformation) + ",年龄错误"

#作为独立文件运行
if __name__=='__main__':
    age=int(input('请输入年龄:'))

#输入一个数据，如果正常，那就正常执行；如果错误，抛出定义的异常
if age<0 or age>130:
    raise AgeError(age)
else:
    print("年龄是：",age)
