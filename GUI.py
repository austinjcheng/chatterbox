from Tkinter import *

def sendMessage():
    sendMessage(entry.get())
    entry.delete(0, END)

root = Tk()

entry = Entry(root)
chat = Text(root, height=2, width=30)

entry.grid(row=1, column=1)
chat.grid(row=0, column=1)

#entry.bind('<Tab>', hello)

Button(root, text='Enter', command=sendMessage).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )











"""
from Tkinter import *

def sendMessage():
    return

root = Tk()
root.title("Chatterbox")

w = Label(root, text="Hello Tkinter!")
w.pack()

entry = Entry(root)

Button(root, text='Enter', command=sendMessage).grid(row=0, column=1, sticky=W, pady=4)

root.mainloop()
"""