# coding=utf-8
"""
调用父类的方法
"""

"""
你想在子类中调用父类的某个已经被覆盖的方法
"""


class A:
    def spam(self):
        print('A.spam')


class B(A):
    def spam(self):
        print('B.spam')
        super().spam()  # Call parent spam


b = B()
b.spam()
"""
super()函数的一个常用方法就是在__init__()方法中确保父类被正常的初始化了:
"""


class C:
    def __init__(self):
        self.x = 0

    def add(self, x, y):
        print(x + y)

    @property
    def num(self):
        return 6 + 7


class D(C):
    def __init__(self):
        super(D, self).__init__()  # python 中的继承不会自动的调用父类的构造函数(不像C#)
        self.y = 1


d = D()
d.add(3, 5)
print(d.num)
print(d.x)

"""
super()的另外一个常见用出现在付给Python的特殊方法的代码中(我的理解其实就是调用object父类的方法)
"""


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, key, value):
        if key.startswith('-'):
            super().__setattr__(key, value)  # call original __setattr__
        else:
            setattr(self._obj, key, value)


class Base:
    def __init__(self):
        print('Base.__init__')


class E(Base):
    def __init__(self):
        super().__init__()
        print('E.__init__')


class F(Base):
    def __init__(self):
        super().__init__()
        print('F.__init__')


class G(E, F):
    def __init__(self):
        super().__init__()  # Only one call to super() here
        print('G.__init__')


g = G()
print(G.__mro__)
