from Tkinter import *
from Socket import sendMessage

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
        root = Tk()
        scrollbar = Scrollbar(root)
        self.chat = Text(root, height=4, width=50)
        entry = Entry(root)
        entry.pack(side=BOTTOM)
                    
        scrollbar.pack(side=RIGHT, fill=Y)
        self.chat.pack(side=LEFT, fill=Y)
                    
        scrollbar.config(command=self.chat.yview)
        self.chat.config(yscrollcommand=scrollbar.set)

    def startGUI(self):
        mainloop()
        
        
    def displayMessage(self, string):
        self.chat.insert(END, string)
    
    def sendMessage(self):
        Socket.sendMessage(entry.get())
        entry.delete(0, END)




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