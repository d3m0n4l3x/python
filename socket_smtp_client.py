#!/usr/bin/python
#Written by CHAOYI HUANG in Python 3.7.0
from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = '192.168.3.68'		#the internal IP address of an internal SMTP server

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')
	exit()

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
print "Sending:", heloCommand
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
	print('250 reply not received from server.')
	exit()

# Send MAIL FROM command and print server response.
mailFromCommand = 'MAIL FROM: <chaoyi.huang@gmail.com>\r\n'
print "Sending:", mailFromCommand
clientSocket.send(mailFromCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
	print('250 reply not received from server.')
	exit()

# Send RCPT TO command and print server response.
rcptToCommand = 'RCPT TO: <itsecurity@aaa.com>\r\n'
print "Sending:", rcptToCommand
clientSocket.send(rcptToCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
	print('250 reply not received from server.')
	exit()

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
print "Sending:", dataCommand
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
	print('354 reply not received from server.')
	exit()

# Send message data.
print "Sending:", msg
clientSocket.send(msg.encode())
print "\r\n"

# Message ends with a single period.
print "Sending:", endmsg
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
	print('250 reply not received from server.')
	exit()

# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
print "Sending:", quitCommand
clientSocket.send(quitCommand.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '221':
	print('221 reply not received from server.')
	exit()

exit()
