a=[1,2,3,4,5]
b=(x**3 for x in a)
for i in b:
    print(i,end=' ')

print('\n')

list1=[1,2,3,4,5,6]
list2=[7,8,9,10,11,12]
c=[x*y for x in list1 for y in list2]
print(c,end='\n\n')

d=[x+y for x in list1 for y in  list2 if x>3 and y>8]
print(d,end='\n\n')

e= [str(round(355/113, i)) for i in range(1, 6)]
print(e)

