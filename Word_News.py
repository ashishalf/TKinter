from msilib.schema import Font
from tkinter import *

from matplotlib.pyplot import text

root=Tk()
root.geometry("600x444")
root.title("Word News")
Label(text="The Word News", font="lucida 25 bold").pack()
Label(text="Friday February 04, 2022", font="lucida 8 bold").pack()

def word_wrap(text):
    w_text=""
    for i in range(0,len(text)):
        w_text+=text[i]
        if i%100==0 and i!=0:
            w_text+="\n"
    return w_text
texts=[]
for i in range(0,3):
    with open(f"{i+1}.txt") as f:
       text=f.read()
       texts.append(word_wrap(text))

Label(text=texts[0],pady=10).pack()
Label(text=texts[1],pady=10).pack()
Label(text=texts[2],pady=10).pack()

root.mainloop()