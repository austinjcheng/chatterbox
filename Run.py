import string
from Read import getUser, getMessage
from Initialize import createUsers, switchUser, startRooms
from Settings import usernames
import threading
from GUI import GUI


def refreshMessages():
    from Initialize import users, currentUserIndex
    readbuffer = ""
    while True:
        readbuffer = readbuffer + users[currentUserIndex].recv(1024)
        temp = string.split(readbuffer, "\n")
        readbuffer = temp.pop()
            
        for line in temp:
            gui.displayMessage(line)
            user = getUser(line)
            message = getMessage(line)
            gui.displayMessage(user + " typed :" + message)


createUsers()
        
global gui
gui = GUI()
guiThread = threading.Thread(target=gui.startGUI)
guiThread.start()
    
startRooms(gui)
    
messageThread = threading.Thread(target=refreshMessages)
messageThread.start()









            
