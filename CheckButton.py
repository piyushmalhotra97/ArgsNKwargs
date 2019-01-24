from tkinter import *
top = Tk()
top.title("Check Button")
top.geometry("500x500+0+0")

def check():
    a=CheckVar1.get()
    print(a)

def check1():
    b=CheckVar2.get()
    print(b)

CheckVar1 = IntVar()
CheckVar2 = IntVar()

C1 = Checkbutton(top, text="DragonBall", variable = CheckVar1,onvalue = 1,offvalue = 0, command = check())
C2 = Checkbutton(top, text="Naruto", variable = CheckVar2,onvalue = 1,offvalue = 0, command = check1())

C1.pack()
C2.pack()

top.mainloop()
