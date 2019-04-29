from Tkinter import *
from Socket import sendMessage
import threading

"""
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

class GUI:
    
    def __init__(self):
        self.root = Tk()
        self.scrollbar = Scrollbar(self.root)
        self.chat = Text(self.root, height=4, width=50)
        self.entry = Entry(self.root)
        self.entry.pack(side=BOTTOM)
                    
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.chat.pack(side=LEFT, fill=Y)
                    
        self.scrollbar.config(command=self.chat.yview)
        self.chat.config(yscrollcommand=self.scrollbar.set)

    def startGUI(self):
        mainloop()
        
        
    def displayMessage(self, string):
        self.chat.insert(END, string)
    
    def sendMessage(self):
        Socket.sendMessage(self.entry.get())
        self.entry.delete(0, END)




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