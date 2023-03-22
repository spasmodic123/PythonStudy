with open(r"C:\Python123pro\picture.png","rb") as f:
    with open("pic_copy.png","wb") as g:
        #line=f.read() 也可以
        for line in f.readlines():#readlines函数用于读取文件中的所有行，它和调用不指定 size 参数的 read() 函数类似，只不过该函数返回是一个字符串列表，其中每个元素为文件中的一行内容
            g.write(line)
print("picture copy succes")