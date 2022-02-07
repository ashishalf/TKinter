from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry('444x333')

def select():
        messagebox.showinfo("Thank You", "Thank You For Select A Language")
    


Label(root, text="Select a language", font="lucida 15 bold").pack(anchor="w")
var=IntVar()
Radiobutton(root, text="C", variable=var, value=1).pack(anchor="w")
Radiobutton(root, text="C++", variable=var, value=2).pack(anchor="w")
Radiobutton(root, text="C#", variable=var, value=3).pack(anchor="w")
Radiobutton(root, text="Java", variable=var, value=4).pack(anchor="w")
Radiobutton(root, text="Python", variable=var, value=5).pack(anchor="w")
Button(root, text="Rate", command=select).pack(anchor="w")

root.mainloop()