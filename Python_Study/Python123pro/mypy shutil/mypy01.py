#encoding=utf_8
import shutil
import zipfile

#简单文件拷贝
#shutil.copyfile("1.txt","1copy.txt")

#简单文件夹拷贝,如果mulu已存在,则报异常\
#shutil.copytree("catalogue_1/catalogue_2",",mulu",ignore=shutil.ignore_patterns("*.txt","*.html"))
#ignore=忽略响应后缀名文件拷贝

#压缩,解压缩
#shutil.make_archive("catalogue_1/ya_suo","zip","catalogue_1/catalogue_2")

'''z1=zipfile.ZipFile("ya_suo_zipfile.zip",'w')
z1.write("1.txt")
z1.write("catalogue_1/catalogue_2/aaa.html")
z1.close()'''

'''z2=zipfile.ZipFile("ya_suo_zipfile.zip")
z2.extractall("jie_ya_suo_zipfile")
z2.close()'''