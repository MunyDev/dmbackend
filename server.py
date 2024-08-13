from http.server import *
import http.client as cli
import requests
import device_management_pb2
import socket
class A(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        dat = self.rfile.read(int(self.headers.get('Content-Length')))
        print("data read")
        print(dat)
        con = requests.request('POST', 'https://m.google.com/devicemanagement/data/api', data=dat)
        self.wfile.write(bytes(str(con.status_code), 'utf-8'))
        # self.wfile.close()
hs = HTTPServer(("0.0.0.0", 3040), A)
hs.serve_forever()
