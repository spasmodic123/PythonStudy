#encoding=utf_8
import shutil
import zipfile

#���ļ�����
#shutil.copyfile("1.txt","1copy.txt")

#���ļ��п���,���mulu�Ѵ���,���쳣\
#shutil.copytree("catalogue_1/catalogue_2",",mulu",ignore=shutil.ignore_patterns("*.txt","*.html"))
#ignore=������Ӧ��׺���ļ�����

#ѹ��,��ѹ��
#shutil.make_archive("catalogue_1/ya_suo","zip","catalogue_1/catalogue_2")

'''z1=zipfile.ZipFile("ya_suo_zipfile.zip",'w')
z1.write("1.txt")
z1.write("catalogue_1/catalogue_2/aaa.html")
z1.close()'''

'''z2=zipfile.ZipFile("ya_suo_zipfile.zip")
z2.extractall("jie_ya_suo_zipfile")
z2.close()'''