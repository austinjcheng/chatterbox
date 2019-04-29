import string
from Socket import sendMessage

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