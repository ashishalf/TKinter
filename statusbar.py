from tkinter import *

top = Tk()
top.geometry("444x333")

def update():
    s.set("Loading..")
    l.update()
    import time
    time.sleep(1)
    s.set("Loading...")


s=StringVar()
s.set("Loading.")
l=Label(top, textvariable=s, relief=SUNKEN,padx=10, anchor="w")
l.pack(side=BOTTOM, fill=X)

Button(top, text="Update", command=update).pack()

top.mainloop()