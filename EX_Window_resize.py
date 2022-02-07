from tkinter import *
root=Tk()
root.geometry('444x444')
def update():
    root.geometry(f"{h.get()}x{w.get()}")
    print("Updated")

w=StringVar()
h=StringVar()

Entry(root, textvariable=w).pack()
Entry(root, textvariable=h).pack()

Button(root, text="Apply", command=update).pack()

root.mainloop()