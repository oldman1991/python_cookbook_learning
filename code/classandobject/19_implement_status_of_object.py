# coding=utf-8
"""
我们想实现一个状态机或者在不同状态下执行操作的对象，但是又不想在代码中
出现太多的条件判断语句
在很多程序中，有些对象会根据某种内部状态来执行不同的操作。比如考虑下面的这个代表网络连接的类:
"""


class ConnectionDemo:
    def __init__(self):
        self.state = 'CLOSED'

    def read(self):
        if self.state != 'OPEN':
            raise RuntimeError('Not Open')
        print('reading')

    def write(self):
        if self.state != 'OPEN':
            raise RuntimeError('Not Open')
        print('writing')

    def open(self):
        if self.state == 'OPEN':
            raise RuntimeError('Already Open')
        self.state = 'OPEN'

    def close(self):
        if self.state == 'CLOSED':
            raise RuntimeError('Already closed')
        self.state = 'CLOSED'


"""
这份代码为我们提出了几个难题.首先,由于代码中引入了许多针对状态的条件检查.代码变得很复杂.
其次,程序的性能下降了.因为普通的操作如读(read())和写(write())总是要在处理前先检查状态.
一个更加优雅的方式是将每种操作状态以一个单独的类来定义.然后再Connection类中使用这些状态类
,实例如下:
"""


class Connection:
    def __init__(self):
        self.new_state(ClosedConnectionState)

    def new_state(self, newstate):
        self._state = newstate

    # Delegate to the state class
    def read(self):
        return self._state.read(self)

    def write(self, data):
        return self._state.write(self, data)

    def open(self):
        return self._state.open(self)

    def close(self):
        return self._state.close(self)


# Connection state base class
class ConnectionState:
    @staticmethod
    def read(conn):
        raise NotImplementedError()

    @staticmethod
    def write(conn, data):
        raise NotImplementedError()

    @staticmethod
    def open(conn):
        raise NotImplementedError()

    @staticmethod
    def close(conn):
        raise NotImplementedError()


# Implementation of different states
class ClosedConnectionState(ConnectionState):
    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)

    @staticmethod
    def write(conn, data):
        raise RuntimeError('Not open')

    @staticmethod
    def close(conn):
        raise RuntimeError('Already Closed')

    @staticmethod
    def read(conn):
        raise RuntimeError('Not open')


class OpenConnectionState(ConnectionState):
    @staticmethod
    def write(conn, data):
        print('writing')

    @staticmethod
    def read(conn):
        print('reading')

    @staticmethod
    def open(conn):
        raise RuntimeError('Already Open')

    @staticmethod
    def close(conn):
        conn.new_state(ClosedConnectionState)


c = Connection()
c._state
# c.read()
c.open()
c._state
c.read()
c.write('hello')
c.close()
c._state

"""
讨论:
"""