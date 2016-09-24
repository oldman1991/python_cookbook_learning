# coding=utf-8
"""
委托属性的访问  8.15
"""
"""
委托实现代理
"""


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, item):
        print('getter:', item)
        return getattr(self._obj, item)

    # Delegate attribute assignment
    def __setattr__(self, key, value):
        if key.startswith('_'):
            super().__setattr__(key, value)
        else:
            print('setter:', key, value)
            setattr(self._obj, key, value)

    # Delegate attribute deletion
    def __delattr__(self, item):
        if item.startswith("_"):
            super().__delattr__(item)
        else:
            print('delattr:', item)
            delattr(self._obj, item)


"""
要使用这个代理,只要简单的用它包装另一个实例就好了,示例如下:
"""


class Spam:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print('Spam.bar:', self.x, y)

s = Spam(2)
p = Proxy(s)

print(p.x)
p.bar(3)
p.x = 37