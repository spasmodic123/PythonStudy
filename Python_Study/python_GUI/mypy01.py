from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("My first GUI")
root.geometry("500x300+200+200")  # 窗口位置

btn01 = Button(root)
btn01["text"] = "点我就送花"
btn01.pack()


def songhua(e):  # e就是事件对象
    messagebox.showinfo("Message", "give you a flower!i love you")
    print("sent ninty nine flower to you")


btn01.bind("<Button-1>", songhua)  # 绑定方法,鼠标左键

root.mainloop()  # 调用组件的mainloop方法,进入事件循环
