from struct import pack
from tkinter import *
root=Tk()
root.geometry("700x450")
def hello():
    print("Hy Buddy, this is a button!")
f=Frame(root, bg="grey", borderwidth=3, relief=SUNKEN, padx=99, pady=33)
f.pack()
b=Button(f, text="Press here!", command=hello)
b.pack()
root.mainloop()