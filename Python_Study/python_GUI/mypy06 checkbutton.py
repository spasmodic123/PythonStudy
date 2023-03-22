import tkinter as tk
from tkinter import messagebox


class Application(tk.Frame):  # Application也是一个组件
    """经典GUI类的写法"""

    def __init__(self, master):
        # 如果子类B和父类A，都写了init方法，
        # 那么A的init方法就会被B覆盖。想调用A的init方法需要用super去调用
        super().__init__(master)  # super()代表的是父类的定义,而不是父类对象
        self.master = master
        self.pack()  # 通过布局管理器显示

        self.createWidget()

    def createWidget(self):
        """ 创建新的组件"""
        self.label01 =tk.Label(text="华哥的食物",font=("宋体",30)).pack()
        self.yudan = tk.IntVar()
        self.youbing = tk.IntVar()
        self.niurouwan = tk.IntVar()
        self.c1 = tk.Checkbutton(text="咖喱鱼蛋",variable=self.yudan,onvalue=1,offvalue=0,font=("黑体",19)).pack()
        self.c2 = tk.Checkbutton(text="肥姨鱼蛋",variable=self.youbing,onvalue=1,offvalue=0,font=("黑体",19)).pack()
        self.c3 = tk.Checkbutton(text="淳淳的鱼蛋",variable=self.niurouwan,onvalue=1,offvalue=0,font=("黑体",19)).pack()

        self.btn01 = tk.Button(text="确定",command=self.confirm,font=("黑体",15)).pack()

    def confirm(self):
        messagebox.showinfo("石锦华的食物", "华哥喜欢吃:{0},{1},{2}".format("咖喱鱼蛋","肥姨鱼蛋","淳淳的鱼蛋"))


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400+200+200")
    root.title("经典GUI 类的测试")
    app = Application(master=root)

    root.mainloop()