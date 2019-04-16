import string
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from Settings import usernames

# Initialize the connection with the given parameters
users = [] # List of logged in users
for i in range(len(usernames) - 1):
    users.append(openSocket(i))
    joinRoom(users[i])

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
        sendMessage(users(0), raw_input("Enter: "))
    
    
    #commmandFile = open("command.txt", 'r')
    #for line in commandFile:
    #    if line in message:

            
