from tkinter import *
root=Tk()
root.geometry('444x444')

def info():
    print(f"The Username is {uservalue.get()}",f"\nThe Password is { pwdvalue.get()}")

    with open("record.txt",'a') as f:
        f.write(f"{uservalue.get(),pwdvalue.get()}")

user=Label(root, text="Username: ")
user.grid()
pwd=Label(root, text="Password: ")
pwd.grid(row=1)

uservalue=StringVar()
pwdvalue=StringVar()

u=Entry(root, textvariable=uservalue)
u.grid(row=0,column=1)
p=Entry(root, textvariable=pwdvalue)
p.grid(row=1, column=1)

Button(text="Submit", command=info).grid()

root.mainloop()
