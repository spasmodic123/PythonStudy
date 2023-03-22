with open(r"C:\Python123pro\poet.txt",'r',encoding="utf-8") as f:
    print(f.read(),end='\n\n')#全部读取

with open(r"C:\Python123pro\poet.txt",'r',encoding="utf-8") as g:
    while True:
        fragment = g.readline()#按行读取
        if not fragment:
            break
        else:
                print(fragment)


with open(r"C:\Python123pro\poet.txt",'r',encoding="utf-8") as h:#使用迭代器读取文件,按行读取
    for i in h:
        print(i)#换行换多了一行,因为文件本身就有换行符,print函数又会加多一个换行符


