import Tkinter
import tkMessageBox
from Tkinter import *

top = Tkinter.Tk()
# Code to add widgets will go here...

L1 = Label(top, text = "User Name")
L1.pack(side = LEFT)
E1 = Entry(top, bd=5)
E1.pack(side = RIGHT)

def helloCallBack():
    tkMessageBox.showinfo( "Hello Python", E1.get() )
B = Tkinter.Button(top, text = "Hello", command = helloCallBack)
B.pack()

top.mainloop()
