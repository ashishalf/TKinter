from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry('444x333')

def update():
    print("Updated")

def help():
    messagebox.showinfo("Help", "This is a simple GUI.")

def rate():
    messagebox.askquestion("Rate Us", "Was your experience good?")

mymenu=Menu(root)
submenu = Menu(mymenu, tearoff=0)
submenu.add_command(label="Save", command=update)
submenu.add_command(label="Save As", command=update)
submenu.add_separator()
submenu.add_command(label="Print", command=update)
submenu1 = Menu(mymenu, tearoff=0)
submenu1.add_command(label="Help", command=help)
submenu1.add_command(label="Rate", command=rate)
root.config(menu=mymenu)
mymenu.add_cascade(label="File", menu=submenu)
mymenu.add_cascade(label="Help", menu=submenu1)
mymenu.add_cascade(label="Exit", command=quit)



root.mainloop()