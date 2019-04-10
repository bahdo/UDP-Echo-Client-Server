import sys
from socket import *

serverIP = "127.0.0.1"
serverPort = 8000
lengthOfString = 10

s = socket(AF_INET, SOCK_DGRAM)
s.bind((serverIP, serverPort))

print("Server ready to receive on Port " + str(serverPort))

while True:
	data, address = s.recvfrom(lengthOfString)
	print("receive data from client "+address[0] + ", " + str(address[1]) + ": " + data.decode())


	print("Sending data to client " + address[0] + ", " + str(address[1]) + ": " + data.decode())
	s.sendto(data, address)