
import SimpleHTTPServer
import BaseHTTPServer
import ssl
import socket

myskt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myskt.connect(("http://png.cybermirror.org", 80))
cmd = "GET http://png.cybermirror.org/spec/iso/iso_8859-1.txt HTTP/1.0\r\n\r\n".encode()
myskt.send(cmd)


while True:
    data = myskt.recv(999)
    if (len(data) < 1):
        break
    print(data.decode())
myskt.close()


httpd = BaseHTTPServer.HTTPServer(
    ('localhost', 4443), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(
    httpd.socket, certfile='./server.pem', server_side=True)
httpd.serve_forever()
