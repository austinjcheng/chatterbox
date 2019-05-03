from Tkinter import *
from Socket import sendDefaultMessage
from Initialize import switchUser
from Settings import usernames


class GUI:
    
    def __init__(self):
        self.currentUserIndex = 0
        
        self.root = Tk()
        self.scrollbar = Scrollbar(self.root)
        self.chat = Text(self.root, height=40, width=100)
        self.entry = Entry(self.root)
        self.entry.bind("<Return>", self.sendMessage)
        self.entry.bind("<Tab>", self.switchUser)
                    
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.chat.pack(side=TOP, anchor=N, fill=BOTH, expand=YES)
                    
        self.scrollbar.config(command=self.chat.yview)
        self.chat.config(yscrollcommand=self.scrollbar.set)
        
        self.usr_btn_text = StringVar()
        self.usr_btn = Button(self.root, textvariable=self.usr_btn_text, command=self.switchUser)
        self.usr_btn_text.set(usernames[0])
        self.usr_btn.pack(side=BOTTOM, anchor=SW)
        self.entry.pack(side=BOTTOM, anchor=SE, fill=X, expand=YES)
        
        self.entr_btn = Button(self.root, text="Enter", command=self.sendMessage)
        self.entr_btn.pack(side=BOTTOM, anchor=SE)
        
    def startGUI(self):
        mainloop()
        
    def displayMessage(self, string):
        self.chat.insert(END, string + "\n")
    
    def sendMessage(self, string=""):
        sendDefaultMessage(self.entry.get())
        self.entry.delete(0, END)
        
    def switchUser(self, string=""):
        self.currentUserIndex += 1
        if self.currentUserIndex >= len(usernames):
            self.currentUserIndex = 0
        self.usr_btn_text.set(usernames[self.currentUserIndex])
        switchUser(self)
        return "break"
        
        
        
        
        
        