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
