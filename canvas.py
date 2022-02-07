from tkinter import *
root=Tk()
root.title("Canvas")
can_width=500
can_height=400
root.geometry(f"{can_width}x{can_height}")
can=Canvas(root, width=can_width,height=can_height)
can.pack()
can.create_line(0,0,can_width,44)
root.mainloop()
