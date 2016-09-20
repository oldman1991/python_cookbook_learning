# coding=utf-8
"""
创建一种新形式的类属性或者实例属性 8.9
"""
"""
如果想创建一个新形式的实例属性,可以以描述符类的形式定义其功能.实例如下:
"""


# Descriptor attribute for an integer type-checked attribute
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


"""
所谓的描述符就是以特殊方法__get__(),__set__()和__delete__()的形式实现的三个核心的属性访问操作(对应于get,set,he delete)的类
这些方法通过接受类实例做为输入来工作.之后,底层的实例字典会根据需要适当的进行调整
"""
"""
要使用一个描述符,我们把描述符的实例放置在类的定义中做为类变量来使用.示例如下:
"""


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(2, 3)
print(p.x)  # calls Point.x.__get__(p,Points)
p.y = 5  # Calls Point.y.__set__(p,5)
"""
描述符常常回座位一个组件出现在大型的编程框架中,其中还会涉及装饰器或者元类.正因为如此,对描述符的使用可能隐藏得很深,几乎看不到痕迹
例如,下面是一些更加高级的基于描述符的代码,其中还用到了类装饰器
"""


class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


# Class decorator that applies it to selected attributes

def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            setattr(cls, name, Typed(name, expected_type))
        return cls

    return decorate


# Example use

@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name,shares, price):
        self.name = name
        self.shares = shares
        self.price = price

print(Stock.__dict__)

"""
最后应该强调的是,如果只是想访问某个特定的 类中的一种属性,并对此做定制化的处理,那么最好不要编写描述符来实现.对于这个
任务,用property属性方法来完成会更加简单.在需要大量重用代码的情况下,描述符会更加有用(例如,我们希望在自己的代码中大量使用
描述符提供的功能,或者将其作为库来使用)
"""