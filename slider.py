from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry('444x333')

def rate():
    print(f"{S.get()}")
    messagebox.showinfo("Thank You", "Thank You For Rate Us.")
    with open("rate.txt","a") as f:
        f.write(f"\nRating of GUI: {S.get()}")

Label(root, text="Rate Our GUI", font="lucida 19 bold").pack()
S=Scale(root, from_=0, to=5, orient=HORIZONTAL, tickinterval=1)
S.pack()
Button(root, text="Rate", command=rate).pack()
Button(root, text="Exit", command=quit).pack(side=LEFT)

root.mainloop()