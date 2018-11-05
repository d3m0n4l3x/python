#!/usr/bin/python3
#Successfully running on Python 3.6.7 with Kali Linux
import socket
import threading

bind_ip="0.0.0.0"
bind_port=8888

def handle_client(client_socket):
    request=client_socket.recv(1024)
    print("Received : %s\n" % request)
    #Utilizing encode() to solve the issue of "a bytes-like object is required, not 'str'":
    client_socket.send('ACK\n'.encode())
    client_socket.close()

def main():
    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip, bind_port))
    server.listen(5)
    print("Listening on %s:%d\n" % (bind_ip, bind_port))
    while True:
        client, addr=server.accept()
        print("Accepted connection from %s:%d\n" % (addr[0], addr[1]))
        client_handler=threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
        
main()
exit()
