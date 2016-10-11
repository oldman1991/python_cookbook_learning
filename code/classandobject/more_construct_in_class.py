# coding=utf-8
"""
在类中定义多个构造器 8.16
你想实现一个类，除了使用__init__()方法外，还有其他方式可以初始化它
"""
import time

"""
为了实现多个构造器，你需要使用类方法，例如：
"""


class Date:
    """"方法一：使用类方法"""

    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


a = Date(2012, 12, 21)  # Primary
b = Date.today()  # Alternate
print(a)
print(b)

"""
类方法的一个主要作用是定义多个构造器，他接收一个class作为第一个参数（cls）.
你应该注意到了这个类被用来创建并返回最终的实例。继承时也能工作的很好：
"""


class NewDate(Date):
    pass


c = Date.today()  # 创建一个Date的实例(cls=Date)
d = NewDate.today()  # create an instance of NewDate (cl=NewDate)
print(c)
print(d)

