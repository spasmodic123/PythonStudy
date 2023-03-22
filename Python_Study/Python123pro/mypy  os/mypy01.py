import os

#os.system("notepad.exe")#打开记事本
#os.system("regedit")#注册表
#os.system("ping www.baidu.com")
#os.system('cmd')

#直接调用可执行文件
#os.startfile(r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe")

#返回path目录下的文件和目录列表
catalogue=os.listdir("C:\Python123pro\mypy")
for i in catalogue:
    if i.endswith("py"):#增加后缀名的判断
        print(i)

filelist=[file_name for file_name in catalogue if file_name.endswith("txt")]
print(filelist) #结合推导式
#获取文件和文件夹的相关信息
#print(os.name)#widnows->nt  linux->posix
#print(os.sep)#windows->|  linux->/
#print(os.linesep)#windows->\r \n
#print(os.stat('C:\Python123pro\mypy'))#获取文件信息

#关于文件目录的操作
#print(os.getcwd())#获取文件的路径
#os.chdir("C:\Python123pro\mypy")#改变工作目录
#os.mkdir("新的子目录")#创建新的子目录

#创建目录,多级目录,删除
#os.rmdir("新的子目录")#删除目录.如果不用chdir指定文件,则相对于当前工作目录
#os.makedirs("1/2/3/4")
#os.removedirs("1/2/3/4")#只能删除空目录,否则出错
#os.makedirs("../上一级目录")