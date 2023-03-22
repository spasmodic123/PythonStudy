#coding=utf-8
import os

all_file=[]

os.chdir("C:\Python123pro")
path=os.getcwd()
list_files=os.walk(path)#返回一个有3个元素的元组

for dirpath,dirnames,filenames in list_files:
    print(dirpath)
    for a in dirnames:
        print((os.path.join(dirpath,a)))#join函数把路径和对应目录名结合,形成绝对路径
    print('\n\n')
    for b in filenames:
          all_file.append(os.path.join(dirpath,b))

#for i in all_file:
    #print(i)
