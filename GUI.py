from Tkinter import *
from Socket import sendDefaultMessage
from Initialize import switchUser
#from Initialize import currentUserIndex
#from Run import getUsers, getCurrentUserIndex


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
        self.chat = Text(self.root, height=40, width=50)
        self.entry = Entry(self.root)
        self.entry.bind("<Return>", self.sendMessage)
        self.entry.bind("<Tab>", switchUser)
        self.entry.pack(side=BOTTOM, fill=X, expand=YES)
                    
        self.scrollbar.pack(side=RIGHT, fill=Y)
        #self.chat.pack(side=LEFT, fill=Y)
        self.chat.pack(side=LEFT, fill=BOTH, expand=YES)
                    
        self.scrollbar.config(command=self.chat.yview)
        self.chat.config(yscrollcommand=self.scrollbar.set)
        

    def startGUI(self):
        mainloop()
        
        
    def displayMessage(self, string):
        self.chat.insert(END, string + "\n")
    
    def sendMessage(self, string):
        sendDefaultMessage(self.entry.get())
        self.entry.delete(0, END)
        
    #def switchUser(self):
        




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