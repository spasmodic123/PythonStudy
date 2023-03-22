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
        self.createWidget()

    def createWidget(self):
        """ 创建新的组件"""



if __name__ == "__main__":
    root = Tk()
    root.geometry("200x400+200+200")
    root.title("经典GUI 类的测试")
    app = Application(master=root)

    root.mainloop()
