# coding=utf-8
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    """返回一个类对象, 将属性都转化为大写形式
    :param future_class_attr:
    :param future_class_parents:
    :param future_class_name:
    """
    #  选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
    #  将他们转化为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)

    #  通过 'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)


__metaclass__ = upper_attr  # 这会作用到这个模块中的所有类


class Foo(object):
    __metaclass__ = upper_attr
    bar = 'Bip'


print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))
