# coding=utf-8
"""
定义一个属性可由用户修改的装饰器 9.5
我们想编写一个装饰器来包装函数,但是可以让用户调整装饰器的属性,这样在运行时能够控制装饰器的行为
引入访问器函数(accessor function),通过使用nonlocal关键字声明变量来修改装饰器内部的属性.
之后把访问器函数作为函数属性附加到包装函数上
"""
import logging
from functools import partial, wraps


def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    """
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message, If name and message aren't specialed,
    they default to a function's module and name.
    """

    def decorate(func):
        logname = name if name else func.__name__
        log = logging.getLogger(logname)
        logmessage = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmessage)
            return func(*args, **wrapper)

        # Attach setter function
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmessage
            logmessage = newmsg

        return wrapper

    return decorate


# Exmple use
@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam')
