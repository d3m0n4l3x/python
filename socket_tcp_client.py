#!/usr/bin/python
import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5354

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((SERVER_IP, SERVER_PORT))

print('Client has been assigned socket name', sock.getsockname())

sock.send('Hi there, server')

message=sock.recv(1024)

print('The server said', message)

sock.close()

