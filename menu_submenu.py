from tkinter import *
root=Tk()
root.geometry('444x333')

def update():
    print("Updated")

# mymenu=Menu(root)
# mymenu.add_command(label="File", command=update)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)

mymenu=Menu(root)
submenu = Menu(mymenu, tearoff=0)
submenu.add_command(label="Save", command=update)
submenu.add_command(label="Save As", command=update)
submenu.add_separator()
submenu.add_command(label="Print", command=update)
root.config(menu=mymenu)
mymenu.add_cascade(label="File", menu=submenu)
mymenu.add_cascade(label="Exit", command=quit)

root.mainloop()