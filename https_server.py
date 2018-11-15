#!/usr/bin/python3
'''
1) Generate the certificate and key by executing the command below:
# openssl req -newkey rsa:2048 -nodes -keyout /root/test/server-key.pem -x509 -days 365 -out /root/test/cert.pem

2)Place the index.html with this Python script before running.

3) Browse https://127.0.0.1/index.html
'''
import http.server
import ssl


Handler = http.server.SimpleHTTPRequestHandler

httpd = http.server.HTTPServer(('', 443), Handler)

httpd.socket = ssl.wrap_socket(httpd.socket, certfile='/root/test/cert.pem', keyfile='/root/test/server-key.pem', server_side=True)

httpd.serve_forever()