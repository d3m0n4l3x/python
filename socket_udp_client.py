#!/usr/bin/python
import socket


UDP_TARGET_HOST='127.0.0.1'
UDP_TARGET_PORT=5354
MAX_BYTES = 65535


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sent_text="Hello"
sent_data = sent_text.encode('ascii')
sock.sendto(sent_data, (UDP_TARGET_HOST, UDP_TARGET_PORT))
recv_data, client_addr = sock.recvfrom(MAX_BYTES)
recv_text = recv_data.decode('ascii')
print('The server {} replied {!r}' .format(client_addr, recv_text))
sock.close()

