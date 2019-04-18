import string
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from Settings import usernames
from pynput import keyboard
import threading

# Initialize the connection with the given parameters
users = [] # List of logged in users
for num, name in enumerate(usernames):
    users.append(openSocket(num))
    joinRoom(users[num])
    
currentUserIndex = [0]
currentUserIndex[0] = 0

def refreshMessages():
    readbuffer = ""
    while True:
        readbuffer = readbuffer + users[currentUserIndex[0]].recv(1024)
        temp = string.split(readbuffer, "\n")
        readbuffer = temp.pop()
            
        for line in temp:
            print(line)
            user = getUser(line)
            message = getMessage(line)
            print(user + " typed :" + message)
"""             
def on_press(key):
    print(key)
    if key == keyboard.Key.tab:
        currentUserIndex[0] += 1
        if currentUserIndex[0] >= len(users):
            currentUserIndex[0] = 0
        print("Switched user to: " + users[currentUserIndex[0]])
"""
def on_press(key):
    try:
        if key == keyboard.Key.tab:
            currentUserIndex[0] += 1
            if currentUserIndex[0] >= len(users):
                currentUserIndex[0] = 0
            print("Switched user to: " + usernames[currentUserIndex[0]])
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
        
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    

messageThread = threading.Thread(target=refreshMessages)
messageThread.start()

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

message = ""
while message.lower() != "exit":
    message = raw_input("Enter: ")
    sendMessage(users[currentUserIndex[0]], message)





            
