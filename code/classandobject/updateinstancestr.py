# coding=utf-8
"""
修改实力的字符串表示
"""


class Pair():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r},{0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s},{0.y!s})'.format(self)

    """
    特殊方法__repr__()返回的是实例的代码表示(code representation),通常可以用它返回的字符串文本重新创建这个实例 即满足 obj==eval(repr(obj))
    内奸的 repr()函数可以用来返回这个字符换,当缺少交互式解释环境时可用它来检查实例的值
    特殊方法__str__()将实例转换为一个字符串,这也是由str()和print()函数所产生的输出.
    """


p = Pair(3, 4)
print(p.__repr__())
print(p)

