# coding=utf-8
"""
我们用node类来表示树结构.也许你想实现一个迭代器能够以深度优先的模式遍历树的节点
"""

class Node:
    def __init__(self,value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_children(self,node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        print('begin')
        yield self
        # print(self)
        print('*'*20)
        for c in self:
            yield from c.depth_first()

if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_children(child1)
    root.add_children(child2)
    child4 = Node(4)
    child1.add_children(Node(3))
    child1.add_children(child4)
    child2.add_children(Node(5))
    child4.add_children(Node(6))
    for ch in root.depth_first():
        print(ch)