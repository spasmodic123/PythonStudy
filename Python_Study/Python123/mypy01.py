import  io


b="wo shi ge liang zai"
sio=io.StringIO(b)
sio.getvalue()
sio.seek(1)
sio.write('h')
sio.getvalue()
print(sio.getvalue())
print(b)

c=[1,2,3,4]
c.pop(0)
print(c)
c.reverse()
print(c)
c.sort()
print(c)

d=list(range(0,50,2))
print(d)