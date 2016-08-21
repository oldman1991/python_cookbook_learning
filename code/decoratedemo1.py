# coding=utf-8
"""
学习装饰器 2016-08-20 by oldman
"""
from functools import wraps

"""
先来看一个简单的装饰器
"""


def decor1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('i am a decorate')

    return wrapper


@decor1
def add(x, y):
    print('result is {}'.format(x + y))


# if __name__  =="__main__":
#     add(2,3)

"""
再来看一个带参数的装饰器
"""


def decor2(parm):
    """
    parm为装饰器用到的参数
    """

    def _decor2(func):  # func为被装饰的函数
        @wraps(func)  # wraps 装饰器会把func的元数据带过来
        def wrapper(*args, **kwargs):
            if parm:
                func(*args, **kwargs)
                print('I am true')
            else:
                print('sorry, false')

        return wrapper

    return _decor2


@decor2(True)  # 这里装饰器的参数为True
def add1(x, y):
    print('result is {}'.format(x + y))


if __name__ == '__main__':
    add1(2, 3)
