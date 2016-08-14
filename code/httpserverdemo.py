# coding=utf-8
from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        buf = 'It works'
        self.protocal_version = "HTTP/1.1"

        self.send_response(200)

        self.send_header("Welcome", "Contect")

        self.end_headers()

        self.wfile.write(buf)

def start_server():
    http_server=HTTPServer(("",9000),RequestHandler)
    http_server.serve_forever()

if __name__ == "__main__":
    start_server()