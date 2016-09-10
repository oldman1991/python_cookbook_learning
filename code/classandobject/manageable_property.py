# coding=utf-8
"""
创建可管理的属性 8.6
"""


class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self.first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not  isinstance(value,str):
            raise TypeError('Excepted a string')
        self.first_name = value

    # Deleter function(optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")

"""
三个函数的名字必须一样
第一个方法是一个getter 它使得first_name 成为一个属性,其他两个方法给fist_name属性添加了setter和deleter函数
需要强调的是只有在first_name被创建之后,后面的两个装饰器@first_name.setter和first_name.deleter才能被定义
"""
print(Person.__dict__)
print(dir(Person))