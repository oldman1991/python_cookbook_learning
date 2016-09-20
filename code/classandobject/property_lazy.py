# coding=utf-8

"""
让属性具有惰性求值的能力 8.10
"""
"""
我们想将一个只读的属性定义为property属性方法,只有在访问他时才参与计算.但是一旦访问了该属性,我们希望把计算出的值缓存起来,
不要每次访问时都重新计算
"""
"""
定义一个惰性属性最有效的方式就是利用描述符类来完成.实例如下:
"""


class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


"""
要使用上面的代码,可以像下面这样在某个类中使用它
"""
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius


# c = Circle(4.0)
# print(Circle.__dict__)
# print(c.radius)
# print(c.area)
# print(c.area)
# print(c.perimeter)
# print(c.perimeter)

"""
请注意,这里的'Computing area' 和 'Computing perimeter'只打印了一次
"""
"""
只有当被访问的属性不在底层的实例字典中, __get__()方法才会被调用,
实例中的lazyproperty类通过__get__()方法以property属性相同的名称来保存计算出的值.这么做会让值保存在实例字典中,可以阻止该property属性
重复进行计算.
"""

"""
这种做法有一个潜在的缺点,即,计算出的值在创建之后就变成可变的(mutable)
"""

"""
如果需要考虑可变性的问题,可以使用另外一种方式实现,但是执行效率会稍打折扣
"""


def lazypropertydef(func):
    name = '__lazy__' + func.__name__

    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            valus = func(self)
            setattr(self, name, valus)
            return valus

    return lazy


class Circle1:
    def __init__(self, radius):
        self.radius = radius

    @lazypropertydef
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazypropertydef
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius

d = Circle1(4.0)
print(d.area)
print(d.area)
print(Circle1.__dict__)
d.area = 4
print(d.area)