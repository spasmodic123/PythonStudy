import pickle

a1='wu bo xiong'
a2=171
a3=(['我是个靓仔'])

with open('pickle.txt','wb')as f:
    pickle.dump(a1,f)
    pickle.dump(a2,f)
    pickle.dump(a3,f)

with open('pickle.txt','rb')as f:
    b1=pickle.load(f)#按照顺序,序列化循序a1a2a3,拿出来也是123
    b2=pickle.load(f)
    b3=pickle.load(f)

print("b1:",b1)
print("b2:",b2)
print("b3:",b3)