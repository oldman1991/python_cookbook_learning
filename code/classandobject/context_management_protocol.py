# coding=utf-8
"""
让对象支持上下文管理协议8.3
"""
from _socket import AF_INET, SOCK_STREAM, socket
from functools import partial


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None


class B(A):
    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None


"""
这个类的核心功能就是表示一条网络连接,但是实际上在初始状态下它并不会做任何事情(比如,他并不会建立一条连接).相反,网络连接是通过with语句
来建立和关闭的(这正是上下问管理的基本要求).示例如下:
"""

# if 1 == 1:
#    print("人生苦短，我用python")

if __name__ == "__main__":
    conn = LazyConnection(('wwww.python.org', 80))
    # Connection closed
    with conn as s:
        # conn.__enter__()executes:connection open
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host:www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))
        # conn.__exit__() executes: connection closed
