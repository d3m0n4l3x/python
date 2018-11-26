#!/usr/bin/env python3
#Generating the certificate and private-key:
#openssl req -newkey rsa:2048 -nodes -keyout ./server-key.pem -x509 -days 3650 -out ./cert.pem
from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl
import base64

username="admin"
password="admin"
secret=username + ":" + password
secret=base64.b64encode(secret.encode())
secret=secret.decode("utf-8")
secret="Basic "+secret

class CustomHandler(BaseHTTPRequestHandler):
    ''' Main class to present webpages and authentication. '''
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm=\"Test\"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        ''' Present frontpage with user authentication. '''
        if self.headers['Authorization'] == None:
            self.do_AUTHHEAD()
            self.wfile.write(bytes('no auth header received', 'UTF-8'))
            pass
        elif self.headers['Authorization'] == secret:
            self.do_HEAD()
            self.wfile.write(bytes(self.headers['Authorization'], 'UTF-8'))
            self.wfile.write(bytes(' authenticated!', 'UTF-8'))
            pass
        else:
            self.do_AUTHHEAD()
            self.wfile.write(bytes(self.headers['Authorization'], 'UTF-8'))
            self.wfile.write(bytes(' not authenticated', 'UTF-8'))
            pass

def main():
    try:
        httpd = HTTPServer(('', 10001), CustomHandler)
        httpd.socket = ssl.wrap_socket(httpd.socket, certfile='cert.pem', keyfile='server-key.pem', server_side=True)
        print ('started httpd at https://0.0.0.0:10001/ ...')
        #print(secret)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print ('^C received, shutting down server')
        httpd.socket.close()

if __name__ == '__main__':
    main()
