# coding=utf-8

"""
简化数据结构的初始化过程 8.11
"""
import math

"""
我们编写了许多类,把他们当做数据结构来用.但是我们厌倦了编写高度重复且样式相同的__init__()函数
通常我们可以将初始化数据结构的步骤归纳到一个单独的__init__()函数中,并将其定义在一个公共的基类中
"""


class Structure:
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


# example
if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']


    class Point(Structure):
        _fields = ['x', 'y']


    class Circle(Structure):
        _fields = ['radius']

        def area(self):
            return math.pi * self.radius ** 2
    s = Stock('ACME', 50, 91.1)
    p = Point(2, 3)
    c = Circle(4.5)
    s2 = Stock('ACME', 50)