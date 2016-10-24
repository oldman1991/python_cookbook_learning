# coding=utf-8
"""
实现访问者模式 8.21
我们需要编写代码来处理或遍历一个由许多不同类型的对象组成的复杂数据结构,每种类型的对象处理的方式都不相同.例如遍历一个树结构,根据遇到的
树节点的类型来执行不同的操作.
本节提到的这个问题常常出现在由大量不同类型的对象组成的数据结构的程序中.为了说明,假设我们正在编写一个表示数学运算的程序.要实现这个功能,
程序中会用到一些类,实例如下:
"""


class Node:
    pass


class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand


class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOperator):
    pass


class Sub(BinaryOperator):
    pass


class Mul(BinaryOperator):
    pass


class Div(BinaryOperator):
    pass


class Negate(UnaryOperator):
    pass


class Num(Node):
    def __init__(self, value):
        self.value = value

