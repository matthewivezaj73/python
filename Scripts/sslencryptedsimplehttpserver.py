#Create SSL cert (follow prompts for customization)
#> openssl req -new -x509 -keyout cert.pem -out cert.pem -days 365 -nodes

#Create heepserver.py
import BaseHTTPServer,SimpleHTTPServer,SSL

cert = "cert.pem"

httpd = BaseHTTPServer.HTTPServer(('192.168.1.10',443),
SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,certfile=cert,server_side=True)
httpd.serve_forever()