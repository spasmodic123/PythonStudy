"""经典GUI程序写法,使用面向对象方式"""

import tkinter as tk
from tkinter import messagebox


class Application(tk.Frame):  # Application也是一个组件
    """经典GUI类的写法"""

    def __init__(self, master=None):
        # 如果子类B和父类A，都写了init方法，
        # 那么A的init方法就会被B覆盖。想调用A的init方法需要用super去调用
        super().__init__(master)  # super()代表的是父类的定义,而不是父类对象
        self.master = master
        self.pack()  # 通过布局管理器显示

        self.createWidget()

    def createWidget(self):
        """ 创建新的组件"""
        self.btn01 = tk.Button(self)  # 传self是因为,Button继承了Frame,Button就是个组件容器
        self.btn01["text"] = "点击我送地狱火"
        self.btn01.pack()
        self.btn01["command"] = self.diyuhuo

        self.btn02 = tk.Button(self, text="QUIT", command=root.destroy)  # destory不加(),因为不是调用
        self.btn02.pack()  # btn02不加(),因为不是调用

    def diyuhuo(self):
        messagebox.showinfo("傻逼", "送地狱火,老铁666")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400+200+200")
    root.title("经典GUI 类的测试")
    app = Application(master=root)

    root.mainloop()
