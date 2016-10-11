# coding=utf-8
"""
创建不调用init方法的实例 8.17
"""
from time import localtime

"""
你想创建一个实例，但是希望绕过__init__()方法。
可以通过__new__()方法创建一个未初始化的实例。例如考虑如下这个类：
"""


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

"""
下面演示如何不调用__init__()方法来创建这个Dat实例：
"""
d = Date.__new__(Date)
print(d)
# print(d.year)  # 会报错的
"""
结果可以看到，这个Date实例的属性year还不存在，所以你需要手动初始化：
"""
data = {'year': 2012, 'month': 8, 'day': 29}
for key, value in data.items():
    setattr(d, key, value)
print(d.year)
"""
当我们在反序列对象或者实现某个类方法构造函数是需要绕过__init__()方法来创建
对象，例如，对于上面的Date来讲，有时候你可能会向下面这样定义一个新的构造函数
today():
"""


class Date1:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = da

    @classmethod
    def today(cls):
        ata = cls.__new__(cls)
        t = localtime()
        ata.year = t.tm_year
        ata.month = t.tm_mon
        ata.day = t.tm_mday
        return ata

"""
当你通过这种非常规方法来创建实例的时候，最好不要直接去访问底层实例字典，
除非你真的清楚所有细节。否则的话，如果这个类使用了__slots__,properties,
descriptors或其他高级技术的时候代码就会失效。而这个时候使用setattr()方法
会让你的代码变得更加通用。
"""