# encoding= utf-8

from tkinter import *
from tkinter import messagebox


class Application(Frame):  # Application也是一个组件
    """经典GUI类的写法"""

    def __init__(self, master=None):
        # 如果子类B和父类A，都写了init方法，
        # 那么A的init方法就会被B覆盖。想调用A的init方法需要用super去调用
        super().__init__(master)  # super()代表的是父类的定义,而不是父类对象
        self.master = master
        self.pack()  # 通过布局管理器显示
        self.hahaha()
        self.createWidget()

    def createWidget(self):
        """ 创建新的组件"""
        self.label01 = Label(self, text="登陆页面", width=10, height=2, font=("楷体", 20))
        self.label01.pack()

        '''账号'''
        self.label02 = Label(self, text="用户名", width=5, height=2, font=("宋体", 10))
        self.label02.pack()

        # StringVar变量绑定到指定的组件中
        # StringVar中变量发生变化,组件也发生变化
        # 组件内容发生变化,StringVar变量也跟着变化
        v1 = StringVar()
        self.entry01 = Entry(self, textvariable=v1)
        v1.set("wu_bo_xiong")  # 组件内容默认
        self.entry01.pack()

        '''密码'''
        self.label03 = Label(self, text="密码", width=5, height=2, font=("宋体", 10))
        self.label03.pack()

        v2 = StringVar()
        self.entry02 = Entry(self, textvariable=v2)
        self.entry02.pack()

        self.btn01 = Button(self, text="login", width=6, height=3, font=("宋体", 10), command=self.login)
        self.btn01.pack()

    def login(self):
        print("id:", self.entry01.get())
        print("password:", self.entry02.get())
        if self.entry01.get()=="wu_bo_xiong" and self.entry02.get()=="112233":
            messagebox.showinfo("Message", "login succeed")
        else:
            messagebox.showinfo("Message", "login fail,please input the right password")

    def hahaha(self):
        print("haaaaaaaaaaaaaaaaaaaaaaa")

if __name__ == "__main__":
    root = Tk()
    root.geometry("400x400+200+200")
    root.title("经典GUI 类的测试")
    app = Application(master=root)

    root.mainloop()
