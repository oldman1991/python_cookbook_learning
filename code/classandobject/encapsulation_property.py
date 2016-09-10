# coding=utf-8
"""
在类中封装属性 8.5
"""


class A:
    def __init__(self):
        self._internal = 0  # An internal attribute
        self.public = 1  # A public attribute

    def public_method(self):
        """
        A public method
        """
        pass

    def _internal_method(self):
        """

        """
        pass


class B:
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        print('I am a private')

    def public_method(self):
        pass
        self.__private_method()

print(B.__dict__)

"""
在类B中似有属性会被分别重命名为_B_private 和 _B_.private_method
这时候你可能会问这样重命名的目的是什么,大难就是继承--这种属性通过继承是无法被覆盖的.比如:
"""

class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1  # Does not override B.__private
        self._private = 2

    # Does not override B.__private_method()
    def __private_method(self):
        pass

    """
    这里,私有名称 __private 和__private_method 被重命名为_C_private 和_C_private_method,
    这个和父类中的名称是完全不同的
    """

print(C.__dict__)
c=C()
c.public_method()
print(c._private)

"""

"""