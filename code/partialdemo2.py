# coding=utf-8
"""
测试回调函数
"""
from functools import partial


def apply_async(fun, args, *, callback):
    # Compute the result
    result = fun(*args)

    # Invoke the callback with the result
    callback(result)


def print_result(result):
    print('Got:', result)


def add(x, y):
    return x + y


# apply_async(add,(2,3),callback=print_result) # 对这里有疑问的话可以看7.2 (编写只接受关键字参数的函数)


"""
毁掉函数中携带额外的状态(我们希望回调函数可以同其他变量或者部分环境进行交互)
"""
"""
下面这个例子是使用绑定方法而不是普通的函数
"""


class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got:{}'.format(self.sequence, result))


# r = ResultHandler()
# apply_async(add,(2,3),callback=r.handler)
# apply_async(add,(2,3),callback=r.handler)

"""
使用闭包
"""


def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got:{}'.format(sequence, result))

    return handler


# handler = make_handler()
# apply_async(add, (2, 3), callback=handler)
# apply_async(add, (2, 3), callback=handler)

"""
使用协程(coroutine)
"""


def make_handler_coro():
    sequence = 0
    while True:
        result = yield  # 不得不说这个代码写的是多么的巧妙
        sequence += 1
        print('[{}] Got:{}'.format(sequence, result))


# handler = make_handler_coro()
# next(handler)
# apply_async(add, (2, 3), callback=handler.send)
# apply_async(add, (2, 4), callback=handler.send)

# handler = make_handler_coro()
# next(handler)
# next(handler)

"""
对比一下普通的迭代器(要理解send方法)
"""


def make_handler_yield():
    sequence = 0
    while True:
        yield sequence
        sequence += 1


# handler = make_handler_yield()
# print(next(handler))
# print(next(handler))

"""
使用partial()方法
"""


class SequenceNo():
    def __init__(self):
        self.sequence = 0


def handler(result, seq):
    seq.sequence += 1
    print('[{}] Got: {}'.format(seq.sequence, result))

seq = SequenceNo()
apply_async(add,(2,3),callback=partial(handler,seq=seq)) # partial的具体用法详见7.8 当partial()方法中传入的参数不是按位置来传入的时间要指定参数名
