import tkinter as tk
import random
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
        self.canva = tk.Canvas(width=400, height=400, bg="blue")
        self.canva.pack()

        line = self.canva.create_line(30, 30, 66, 100)  # x坐标,y坐标
        rec = self.canva.create_rectangle(50, 20, 300, 300)
        ov = self.canva.create_oval(50, 20, 300, 300)

        global photo
        photo = tk.PhotoImage(file="picture/1678325680633.png")
        image = self.canva.create_image(100, 170, image=photo)  # 图像的坐标

        btn01 = tk.Button(text="任意创建10个矩形", command=self.create_juxing).pack(side="right")

    def create_juxing(self):
        for i in range(10):
            a = random.randint(1, 100)
            b = random.randint(1, 400)
            c = random.randint(1, int(self.canva["width"]))
            d = random.randint(1, int(self.canva["width"]))
            rec = self.canva.create_rectangle(a, b, c, d)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500+900+200")  # 长x高+横位移+竖位移
    root.title("经典GUI 类的测试")
    app = Application(master=root)

    root.mainloop()
