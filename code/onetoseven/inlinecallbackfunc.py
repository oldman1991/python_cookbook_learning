# coding=utf-8t
"""
内联毁掉函数 7.11
"""
from functools import wraps
from queue import Queue


def apply_async(func,args,*,callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)

"""
现在看看接下来的支持代码,这里涉及一个async类和inlined_async装饰器
"""
class Async:
    def __init__(self,func,args):
        self.func=func
        self.args=args

def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f=func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func,a.args,callback=result_queue.put)
            except StopIteration:
                break
    return wrapper