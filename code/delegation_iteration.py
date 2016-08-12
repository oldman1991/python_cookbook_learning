# coding=utf-8

"""
委托迭代
"""


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_children(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


# Example
"""
在这个例子中,__iter__()方法只是简单的将迭代请求转发给对象内部持有的_children属性上
"""
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_children(child1)
    root.add_children(child2)
    for ch in root:
        print(ch)
