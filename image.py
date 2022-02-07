#add image in TK

# from tkinter import *
# from PIL import Image, ImageTk
# ashish_root=Tk()

# ashish_root.geometry("444x444")
# ashish_root.mainloop()

# # photo=PhotoImage(file="p.png")
# img=Image.open("D:\My Collection\CODINGFIZZ.png")
# photo=ImageTk.PhotoImage(img)

# p=Label(image=photo)
# p.pack()

from tkinter import *
from PIL import Image,ImageTk
import os
root=Tk()
root.geometry("300x300")
image=Image.open("1.png")
photo=ImageTk.PhotoImage(image)
label = Label(image = photo)
label.pack()
dirs=os.listdir()
label2=Label(text=dirs)
label2.pack()
root.mainloop()
