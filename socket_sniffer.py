#!/usr/bin/python
import socket

#Change TCP to UDP by changing socket.IPPROTO_TCP below to socket.IPPROTO_UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

while True:
	print sock.recvfrom(65535)

sock.close()

