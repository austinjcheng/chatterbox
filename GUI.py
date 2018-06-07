from Tkinter import *

def sendMessage():
    return

root = Tk()
root.title("Twitch Spammer")

w = Label(root, text="Hello Tkinter!")
w.pack()

entry = Entry(root)

Button(root, text='Enter', command=sendMessage).grid(row=0, column=1, sticky=W, pady=4)

root.mainloop()