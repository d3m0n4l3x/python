#!/usr/bin/python
import socket
import ssl
import sys

if sys.argv[1]=='':
    print("Usage: test.py hostname\n")
    exit()

hostname = sys.argv[1]
context = ssl.create_default_context()

sock = socket.create_connection((hostname, 443))
ssock=context.wrap_socket(sock, server_hostname=hostname)
print(ssock.version())

exit()