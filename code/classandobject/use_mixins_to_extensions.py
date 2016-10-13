# coding=utf-8
"""
利用mixins扩张类功能
"""

"""
你有很多的方法，想使用它们来扩展其他类的功能。但是这些类并没有任何继承的关系。
因此你不能简单的将这些方法放入一个基类，然后被其他类继承。

通常当你想自定义类的时候会碰上这些问题。可能是某个库提供了一些基础类，
你可以利用他们来构造你自己的类
假设你想扩展映射对象，给他们添加日志，唯一性设置，类型检查等等功能。
下面是一些混入类：
"""


class LoggedMappingMixin:
    """
    Add logging to get/set/delete operations for debugging
    """
    __slots__ = ()  # 混入类都没有实例变量，因为直接实例化混入类没有任何意义

    def __getitem__(self, item):
        print('Getting ' + str(item))
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return super().__delitem__(key)


class SetOnceMappingMixin:
    """
    Only allow a key to be set once
    """
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + "already set")
        return super().__setitem__(key, value)


class StringKeysManppingMixin():
    """
    Restrict keys to string only
    """
    __slots__ = ()

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('keys must be strings')
        return super().__setitem__(key, value)


# a = StringKeysManppingMixin()
# a['11']=11
# print(a['11'])  # 注：object对象是没有__setitem__方法的，所以这里会报错
# print(a)
"""
这些类单独使用起来没有任何的意义，事实上如果你去实例化任何一个类，除了
产生异常外没任何作用。他们是通过多继承和其他映射对象混入使用的，例如：
"""


class LoggedDict(LoggedMappingMixin, dict):
    pass


d = LoggedDict()
d['x'] = 23
print(d['x'])
del d['x']

from collections import defaultdict


class SetOnceDefaultDict(SetOnceMappingMixin, defaultdict):
    pass


d = SetOnceMappingMixin(list)
d['x']