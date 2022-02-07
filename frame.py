from struct import pack
from tkinter import *
root=Tk()
root.geometry("700x450")
f=Frame(root, bg="grey", borderwidth=3, relief=SUNKEN, padx=9, pady=3)
f.pack(side=LEFT, fill="y")
f1=Frame(root, bg="grey", borderwidth=3, relief=SUNKEN, padx=9, pady=3)
f1.pack(side=TOP, fill="x")
Label(f,text="Editor",bg="grey",fg="white",padx=9).pack()
Label(f1,text="Welcome To VS Code 2.0", bg="grey", fg="white",padx=9).pack()
root.mainloop()
