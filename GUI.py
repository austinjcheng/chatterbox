from Tkinter import *
from Socket import sendDefaultMessage
from Initialize import switchUser


class GUI:
    
    def __init__(self):
        self.root = Tk()
        self.scrollbar = Scrollbar(self.root)
        self.chat = Text(self.root, height=40, width=100)
        self.entry = Entry(self.root)
        self.entry.bind("<Return>", self.sendMessage)
        self.entry.bind("<Tab>", switchUser)
        self.entry.pack(side=BOTTOM, fill=X, expand=YES)
                    
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.chat.pack(side=LEFT, fill=BOTH, expand=YES)
                    
        self.scrollbar.config(command=self.chat.yview)
        self.chat.config(yscrollcommand=self.scrollbar.set)
        
        btn_text = StringVar()
        btn = Button(root, textvariable=btn_text, command=switchUser)
        btn_text.set("a")
        

    def startGUI(self):
        mainloop()
        
        
    def displayMessage(self, string):
        self.chat.insert(END, string + "\n")
    
    def sendMessage(self, string):
        sendDefaultMessage(self.entry.get())
        self.entry.delete(0, END)