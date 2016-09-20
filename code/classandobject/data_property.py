# coding=utf-8

"""
数据装饰符
https://docs.python.org/3/howto/descriptor.html


If an object defines both __get__() and __set__(), it is considered a data descriptor.
Descriptors that only define __get__() are called non-data descriptors (they are typically used for methods but other uses are possible).

Data and non-data descriptors differ in how overrides are calculated with respect to entries in an instance’s dictionary.
If an instance’s dictionary has an entry with the same name as a data descriptor, the data descriptor takes precedence.
If an instance’s dictionary has an entry with the same name as a non-data descriptor, the dictionary entry takes precedence.

如果一个对象定义__get__()和__set__()，它被认为是一个数据描述符。只有__get__()描述符定义称为非数据描述符（他们通常用于方法但其他用途是可能的）。
数据和非数据描述符的不同方面如何重写条目的字典计算实例。如果一个实例的字典具有与数据描述符相同的名称的条目，则数据描述符将优先。
如果一个实例的字典具有与非数据描述符相同的名称的条目，则字典条目优先。

"""


class dataproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return 50

    def __set__(self, instance, value):
        pass


class Demo:
    def __init__(self, name):
        self.name = name

    @dataproperty
    def name(self):
        return 'aaaa'


demo = Demo(444)

print(demo.name)