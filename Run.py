import string
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from Settings import usernames
import threading

def refreshMessages():
    readbuffer = ""
    while True:
        readbuffer = readbuffer + users[0].recv(1024)
        temp = string.split(readbuffer, "\n")
        readbuffer = temp.pop()
            
        for line in temp:
            print(line)
            user = getUser(line)
            message = getMessage(line)
            print(user + " typed :" + message)

# Initialize the connection with the given parameters
users = [] # List of logged in users
for num, name in enumerate(usernames):
    users.append(openSocket(num))
    joinRoom(users[num])
    
    
messageThread = threading.Thread(target=refreshMessages)
messageThread.start()

message = ""
while message.lower() != "exit":
    message = raw_input("Enter: ")
    sendMessage(users[0], message)





            
