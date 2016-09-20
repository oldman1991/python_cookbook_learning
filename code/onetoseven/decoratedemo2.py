# coding=utf-8
from functools import wraps


def deco(func):
    @wraps(func)
    def wraps_func(*args, **kwargs):
        print('hahahah')
        return func(*args, **kwargs)

    return wraps_func


class Demo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, a, b):
        return a + b


print(Demo.__dict__)
