# coding=utf-8
from functools import partial
from socketserver import StreamRequestHandler, TCPServer


# class EchoHandler(StreamRequestHandler):
#     def handle(self):
#         print(111)
#         for line in self.rfile:
#             self.wfile.write(b'GOT:'+line)
#
# serv = TCPServer(('',15000),EchoHandler)
# serv.serve_forever()


class EchoHandler(StreamRequestHandler):
    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super().__init__(*args, **kwargs)

    def handle(self):
        for line in self.rfile:
            self.wfile.write(self.ack + line)


serv = TCPServer(('', 15001), partial(EchoHandler, ack=b'RECEVIED:'))
serv.serve_forever()
