import sys
import socket

argv = sys.argv
hostIP = argv[1]
hostPort = argv[2]
length = argv[3]

hostPort = int(hostPort)
length = int(length)
data = 'X' * length

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.settimeout(1.0);

i=0

while i < 3:
	print("Sending to " + hostIP + ", " + str('hostPort') + ": " + data)
	clientSocket.sendto(data.encode(), (hostIP, hostPort))
	try:
		dataEcho, address = clientSocket.recvfrom(length)
		print("Receive data from " + address[0] + ", " + str(address[1]) + ": " + dataEcho.decode())
	except socket.timeout, e:
		error = e.args[0]
		if error == 'timed out':
			print('time out')
		else:
			print e
			sys.exit(1)
	except socket.error, e:
		print e
		sys.exit(1)
	else:
		print('time out')
		sys.exit(1)

	i+=1;




#except socket.timeout, e:
#	print e
#	sys.exit(1)

clientSocket.close()