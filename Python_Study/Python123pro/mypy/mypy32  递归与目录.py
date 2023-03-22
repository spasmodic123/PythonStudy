#encoding=utf-8
import os

correct_sequence_file=[]

def get_all_files(path,level):
    child_files =os.listdir(path)
    for i in child_files:
        file_path=os.path.join(path,i)
        if os.path.isdir(file_path):
            get_all_files(file_path,level+1)#如果是目录而不是文件,继续递归,找文件
        correct_sequence_file.append("\t"*level+file_path)#用一个level制表符控制缩进

get_all_files(r"C:\Python123pro\mypy  os",1)

correct_sequence_file.reverse()#因为函数先进后出,后进先出,原本的顺序相反,需要倒置
for j in correct_sequence_file:
    print(j)