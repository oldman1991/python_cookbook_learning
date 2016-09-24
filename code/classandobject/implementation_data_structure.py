# coding=utf-8
"""
实现一种数据结构 8.13
"""
"""
我们想定义各种各样的数据结构,但是对于某些特定的属性,我们想对允许赋给他们的值强制添加一些限制
"""
"""
下面的代码使用描述符实现了一个类型系统以及对值进行检查的框架
"""


class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


# Descriptor for enforcing type
class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('expected ' + str(self.expected_type))
        super().__set__(instance, value)


# Descriptor for enforcing values
class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected>=0')
        super().__set__(instance, value)


class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) > self.size:
            raise ValueError('size must be <' + str(self.size))
        super().__set__(instance, value)


"""
这些类可作为构建一个数据模型或者系统类型系统的基础组件.让我们继续,下面的这些代码实现了一些不同类型的数据
"""


class Integer(Typed):
    expected_type = int


class UnsignedInteger(Integer, Unsigned):
    pass


class Float(Typed):
    expected_type = float


class UnsignedFloat(Float, Unsigned):
    pass


class String(Typed):
    expected_type = str


class SizedString(String, MaxSized):
    pass


"""
有了这些类型对象,现在就可以像这样定义一个类了
"""


class Stock:
    # Specify constraints
    name = SizedString('name', size=8)
    shares = UnsignedInteger('shares')
    price = UnsignedFloat('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


"""
有了这些约束之后,就会发现现在对属性进行复制是会进行校验的,示例如下
"""
s = Stock('ACME', 50, 91.1)
print(s.name)
s.shares = 75
# s.shares = - 10  ValueError: Expected>=0
# s.price = 'a lot'  TypeError: unorderable types: str() < int()
# s.name  = 'ABRAKLSJDKLSAJDKLSJALKD'  ValueError: size must be <8
"""
可以运用一些技术来简化在类中设定约束的步骤.一种方法是使用类装饰器,示例如下:
"""


# Class decorator to apply constraints

def check_attributes(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key, value(key))
        return cls

    return decorate


# Example
@check_attributes(name=SizedString(size=8), shares=UnsignedInteger, price=UnsignedFloat)
class Stock1:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


"""
另一种方法是使用元类,示例如下
"""


# A metaclass that applies checking
class checkedmeta(type):
    def __new__(cls, clsname, bases, methods):
        # Attach attribute names to the descriptors
        for key, value in methods.items():
            if isinstance(value, Descriptor):
                value.name = key
        return type.__new__(cls, clsname, bases, methods)


# Example
class Stock2(metaclass=checkedmeta):
    name = SizedString(size=8)
    shares = UnsignedInteger()
    price = UnsignedFloat()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
