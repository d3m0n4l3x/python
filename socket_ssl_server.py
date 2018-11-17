#!/usr/bin/python3
import socket
import ssl

SERVER_IP = '0.0.0.0'
SERVER_PORT = 5354

#Generate the certificate and the key:
## openssl req -newkey rsa:2048 -nodes -keyout /root/test/server-key.pem -x509 -days 365 -out /root/test/cert.pem
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('/root/test/cert.pem', '/root/test/server-key.pem')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((SERVER_IP, SERVER_PORT))

sock.listen(1)

ssock=context.wrap_socket(sock, server_side=True)

while True:
    print('Ready to serve...')

    #Prevent SSL: TLSV1_ALERT_UNKNOWN_CA error
    try:
        client_sock, client_addr = ssock.accept()
        message = client_sock.recv(1024)
        print('message:', message)
        client_sock.send('Over!'.encode())
        client_sock.close()
    except ssl.SSLError:
        continue

ssock.close()
sock.close()