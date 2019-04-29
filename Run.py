import string
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from Settings import usernames
from pynput import keyboard
from GUI import *
import threading


gui = GUI()
gui.startGUI()

currentUserIndex = [0]
currentUserIndex[0] = 0

# Initialize the connection with the given parameters
users = [] # List of logged in users
for num, name in enumerate(usernames):
    users.append(openSocket(num))
    joinRoom(users[num], gui)
    
    


"""
root = Tk()

scrollbar = Scrollbar(root)
entry = Entry(root)
chat = Text(root, height=2, width=30)

scrollbar.pack(side=RIGHT, fill=Y)
chat.pack(side=LEFT, fill=Y)

scrollbar.config(command=chat.yview)
chat.config(yscrollcommand=scrollbar.set)

entry.grid(row=1, column=1)
chat.grid(row=0, column=1)


mainloop()
#entry.bind('<Tab>', hello)

#Button(root, text='Enter', command=sendMessage).grid(row=3, column=1, sticky=W, pady=4)

"""

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
"""             
def on_press(key):
    print(key)
    if key == keyboard.Key.tab:
        currentUserIndex[0] += 1
        if currentUserIndex[0] >= len(users):
            currentUserIndex[0] = 0
        print("Switched user to: " + users[currentUserIndex[0]])

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
    """
messageThread = threading.Thread(target=refreshMessages)
messageThread.start()



"""
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()
    
    message = ""
    while message.lower() != "exit":
        message = raw_input("Enter: ")
        sendMessage(users[currentUserIndex[0]], message)
"""


            
