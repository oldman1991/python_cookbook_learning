# coding=utf-8
"""
调用对象上的方法,方法名以字符串形式给出8.20
"""
"""
question: 我们想调用对象上的某个方法,现在这个方法名保存在字符串中,我们想通过它来调用该方法
对于简单情况,可能会使用getattr(),示例如下:
"""
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


p = Point(2, 3)
d = getattr(p, 'distance')(0, 0)
print(d)

"""
另一种方法是使用operator.methodcaller()
实例如下:
"""
import operator

print(operator.methodcaller('distance', 0, 0)(p))

"""
如果想通过名称来查询方法并提供同样的参数反复调用该方法,那么operator.methodcall()是很有用的.
例如,如果你要对一整列点对象排序:
"""
points = [
    Point(1, 2),
    Point(3, 0),
    Point(10, -3),
    Point(-5, -7)
]


# Sort by distance from origin(0,0)
points.sort(key=operator.methodcaller('distance', 0, 0))
