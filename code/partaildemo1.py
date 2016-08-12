# coding=utf-8
from functools import partial
from socketserver import StreamRequestHandler, TCPServer
from urllib.request import urlopen

"""
学习 partial方法  (让带有N个参数的可调用对象以较少的参数形式调用)
"""

# class EchoHandler(StreamRequestHandler):
#     def handle(self):
#         print(111)
#         for line in self.rfile:
#             self.wfile.write(b'GOT:'+line)
#
# serv = TCPServer(('',15000),EchoHandler)
# serv.serve_forever()


# class EchoHandler(StreamRequestHandler):
#     def __init__(self, *args, ack, **kwargs):
#         self.ack = ack
#         super().__init__(*args, **kwargs)
#
#     def handle(self):
#         for line in self.rfile:
#             self.wfile.write(self.ack + line)
#
#
# serv = TCPServer(('', 15001), partial(EchoHandler, ack=b'RECEVIED:'))
# serv.serve_forever()



"""
用函数代替只有单个方法的类

"""


class UrlTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(**kwargs))


# Example use .Download stock data from yahoo

yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo.open(names='IBM,AAPL,FB', fields='sllclv'):
    print(line.decode('utf-8'))

# 这个类可以用一个简单的函数来取代

def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(**kwargs))
    return opener
# Example use
yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo.open(names='IBM,AAPL,FB', fields='sllclv'):
    print(line.decode('utf-8'))