#!/usr/bin/python3
import socket
import ssl

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5354

context = ssl.create_default_context()
context.check_hostname=False
context.verify_mode=ssl.CERT_NONE

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssock=context.wrap_socket(sock, server_hostname=SERVER_IP)

ssock.connect((SERVER_IP, SERVER_PORT))

print('Client has been assigned socket name', ssock.getsockname())

ssock.send('Hi there, server'.encode())

message=ssock.recv(1024)

print('The server said', message)

ssock.close()
sock.close()
exit()