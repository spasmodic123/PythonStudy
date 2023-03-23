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
        self.photo = [PhotoImage(file="C:\Python_Study\python_GUI\picture\\"+str(i+1)+".png") for i in range(10)]
        self.puke = [Label(self.master,image=self.photo[i]) for i in range(10)]

        for i in range(10):
            self.puke[i].place(y=160, x=50*i)
            # 为所有的label增加事件处理
            self.puke[i].bind_class("Label","<Button-1>",self.chupai)
    def chupai(self,event):
        print(event.widget.winfo_geometry())
        print(event.widget.winfo_y())

        if event.widget.winfo_y() == 160:
            event.widget.place(y=20)
        else:
            event.widget.place(y=160)


if __name__ == "__main__":
    root = Tk()
    root.geometry("600x400+200+200")
    root.title("经典GUI 类的测试")
    app = Application(master=root)

    root.mainloop()
