
#导入traceback
import traceback
#产生一个错误
try:
    a=1
    b=2
    print(c)

#将错误打印到文件里
except:
    with open("input  text.txt", "a") as f:
        traceback.print_exc(file=f)
