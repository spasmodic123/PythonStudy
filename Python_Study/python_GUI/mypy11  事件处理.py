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
        self.c1 = Canvas(root, width=300, height=300, bg="green")
        self.c1.pack()

        self.c1.bind("<Button-1>", self.mouse_test)
        self.c1.bind("<B1-Motion>",self.mouse_darg)
        root.bind("<KeyPress>",self.key_board_test)
        root.bind("<KeyPress-a>",self.press_a_test)
        root.bind("<  KeyRelease-a>",self.release_a_test)

    def mouse_test(self, event):  # 测试鼠标左键单击
        print("鼠标左键单击的位置为 {0},{1} (相对于父容器)".format(event.x, event.y))
        print("该事件绑定的组件为 {0}".format(event.widget))

    def mouse_darg(self, event):  # 测试鼠标左键按住拖动
        self.c1.create_oval(event.x, event.y, event.x + 1, event.y + 1)

    def key_board_test(self, event):  # 测试键盘输入
        print("keyboard_char {0} ,keyboard_code {1} ,keysym {2} ".format(event.char, event.keycode, event.keysym))

    def press_a_test(self, event):
        print("press a")

    def release_a_test(self, event):
        print("release a")


if __name__ == "__main__":
    root = Tk()
    root.geometry("600x400+200+200")
    root.title("经典GUI 类的测试")
    app = Application(master=root)

    root.mainloop()  # 主循环
