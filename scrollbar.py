from tkinter import *

top = Tk()
top.geometry("444x333")

s=Scrollbar(top)
s.pack(side=RIGHT, fill=Y)

lb1 = Listbox(top, yscrollcommand=s.set)
for i in range(200):
    lb1.insert(END, f'{i}')

lb1.pack(fill="both")
s.config(command=lb1.yview)

top.mainloop()