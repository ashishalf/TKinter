from tkinter import *
root=Tk()
root.geometry("444x444")
root.title("My GUI")
#text, bg, fg, font, borderwidth,padx,pady
label_attribute=Label(text='''Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation.\n Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[30]\n Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming.\n It is often described as a "batteries included" language due to its comprehensive standard library.[31][32]\nGuido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.\n[33] Python 2.0 was released in 2000 and introduced new features, such as list comprehensions and a cycle-detecting garbage collection system (in addition to reference counting). \nPython 3.0 was released in 2008 and was a major revision of the language that is not completely backward-compatible.\n Python 2 was discontinued with version 2.7.18 in 2020.''',bg="black", fg="white", font="comicsans 12 bold", borderwidth=3, padx=20, pady=100, relief=SUNKEN)

#anchor, fill, side
label_attribute.pack(anchor='nw', fill='y', side=LEFT)

root.mainloop()
