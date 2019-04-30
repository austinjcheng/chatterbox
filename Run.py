import string
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from Settings import usernames
from pynput import keyboard
import threading
from GUI import GUI


def refreshMessages():
    readbuffer = ""
    while True:
        readbuffer = readbuffer + users[currentUserIndex[0]].recv(1024)
        temp = string.split(readbuffer, "\n")
        readbuffer = temp.pop()
            
        for line in temp:
            gui.displayMessage(line)
            user = getUser(line)
            message = getMessage(line)
            gui.displayMessage(user + " typed :" + message)


def main():
    global currentUserIndex
    currentUserIndex = [0]
    currentUserIndex[0] = 0
    
    # Initialize the connection with the given parameters
    global users
    users = [] # List of logged in users
    for num, name in enumerate(usernames):
        users.append(openSocket(num))
        
    
    global gui
    gui = GUI()
    guiThread = threading.Thread(target=gui.startGUI)
    guiThread.start()
    
    for num, name in enumerate(usernames):
        joinRoom(users[num], gui)
    
    messageThread = threading.Thread(target=refreshMessages)
    messageThread.start()
    
def getUsers():
    return users
    
def getCurrentUserIndex():
    return currentUserIndex
    
if __name__ == "__main__":
    main()









            
