import string
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from time import sleep

s = openSocket()
joinRoom(s)
readbuffer = ""

while True:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()
		
		for line in temp:
			print(line)
			if "PING" in line:
				s.send(line.replace("PING", "PONG"))
				break
			user = getUser(line)
			message = getMessage(line)
			print(user + " typed :" + message)

			#commmandFile = open("command.txt", 'r')
			#for line in commandFile:
			#	if line in message:

			if "!commands" in message.lower():
				sendMessage(s, "austin, pyramid")
				break

			if "!austin" in message.lower():
				sendMessage(s, "I love you, " + user)
				break

			if "you suck" in message.lower():
				sendMessage(s, "No, you suck!")
				break
			
			if "!pyramid" in message.lower():
				sendMessage(s, "Kappa")
				sleep(0.5)
				sendMessage(s, "Kappa Kappa")
				sleep(0.5)
				sendMessage(s, "Kappa Kappa Kappa")
				sleep(0.5)
				sendMessage(s, "Kappa Kappa")
				sleep(0.5)
				sendMessage(s, "Kappa")
				break

			if "PogChamp" in message:
				sendMessage(s, "PogChamp")
				break

			if "FeelsBadMan" in message:
				sendMessage(s, "FeelsGoodMan !")
				break

			if "TriHard" in message:
				sendMessage(s, "cmonBruh " + user)
				break

			if "monkaS" in message:
				sendMessage(s, "don't overuse monkas monkaS")
				break
