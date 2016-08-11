# coding=utf-8

"""
将元素映射到序列的元素中(命名元组)
"""
from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('oldman@example.com', '2016-06-13')
# print(sub)
# print(sub.addr)
# print(sub.joined)
# print(len(sub))
# addr, joined = sub
# print(addr, joined)

# namedtuple是不可变的,使用_replace方法修改属性,该方法会创建一个全新的命名元组
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# create a prototype instance
stock_propotype = Stock('', 0, 0.0, None, None)


def dict_to_stock(s):
    return stock_propotype._replace(**s)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(stock_propotype)
print(id(stock_propotype))
b = dict_to_stock(a)
print(b)
print(id(b))
