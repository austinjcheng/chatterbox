import socket
from Settings import HOST, PORT, CHANNEL, usernames, tokens

def openSocket(userIndex):
	
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send("JOIN #" + CHANNEL + "\r\n")
    s.send("PASS " + tokens[userIndex] + "\r\n")
    s.send("NICK " + usernames[userIndex] + "\r\n")
    return s
	
def sendMessage(s, message):
	messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
	s.send(messageTemp + "\r\n")
	print("Sent: " + messageTemp)