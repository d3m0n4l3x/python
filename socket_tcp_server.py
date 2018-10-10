#!/usr/bin/python
import socket

SERVER_IP = '0.0.0.0'
SERVER_PORT = 5354

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((SERVER_IP, SERVER_PORT))

sock.listen(1)

while True:
	print 'Ready to serve...'

	client_sock, client_addr = sock.accept()

	message = client_sock.recv(1024)

	print('message:', message)

	client_sock.send('Over!')

	client_sock.close()


sock.close()

