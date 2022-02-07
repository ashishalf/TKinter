from cProfile import label
from struct import pack
from tkinter import *

ashish_root=Tk()
# change favicon
ashish_root.title("MyGUI")
ashish_root.wm_iconbitmap("1.ico")
#logic of gui

#label
ashish=Label(text="This is my GUI.")
ashish.pack()

#width * Height of window
ashish_root.geometry("733x434") 

#maximum size of window
# ashish_root.maxsize(1222,1000) 

#minimum size of window
# ashish_root.minsize(200,400) 

ashish_root.mainloop()