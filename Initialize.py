import string
from Socket import sendMessage, openSocket
from Settings import usernames

# Loads the previously sent messages when joining a room
def joinRoom(s, gui):
    readbuffer = ""
    Loading = True
    while Loading:
        readbuffer = readbuffer + s.recv(1024)
        temp = string.split(readbuffer, "\n")
        readbuffer = temp.pop()
        
        for line in temp:
            gui.displayMessage(line)
            Loading = loadingComplete(line)
    sendMessage(s, "Successfully joined chat")
    
def loadingComplete(line):
    if("End of /NAMES list" in line):
        return False
    else:
        return True
    
def createUsers():
    global currentUserIndex
    currentUserIndex = 0
    
    global users
    users = []
    for num, name in enumerate(usernames):
        users.append(openSocket(num))
    
def switchUser(self):
    print "Current user is: " + usernames[currentUserIndex]
    global currentUserIndex
    currentUserIndex += 1
    if currentUserIndex >= len(users):
        currentUserIndex = 0
    print "New user is: " + usernames[currentUserIndex]
        
def startRooms(gui):
    for num, name in enumerate(usernames):
        joinRoom(users[num], gui)
        
        
        
        
        
        