#!/usr/bin/python
import socket


UDP_LOCAL_HOST='127.0.0.1'	#'0.0.0.0' represents all interfaces
UDP_LOCAL_PORT=5354
MAX_BYTES = 65535


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_LOCAL_HOST, UDP_LOCAL_PORT))
print('Listening at {}' .format(sock.getsockname()))
while True:
	recv_data, client_addr = sock.recvfrom(MAX_BYTES)
	recv_text = recv_data.decode('ascii')
	print('The client at {} says {!r}' .format(client_addr, recv_text))
	sock.sendto('Olleh', client_addr)
sock.close()
