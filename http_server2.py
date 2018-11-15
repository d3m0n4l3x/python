#!/usr/bin/python3
'''
Place the index.html with this Python script before running.
Browse http://127.0.0.1/index.html
'''
import http.server
import socketserver

PORT = 80
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()