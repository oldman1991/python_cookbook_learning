# coding=utf-8
"""
利用元类来控制实例的创建 9.13
"""
import weakref

"""
实现单利模式
"""


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


# Example
class Spam(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')


a = Spam()
b = Spam()

print(a is b)

c = Spam()
print(a is c)


class Cashed(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self._cache = weakref.WeakKeyDictionary()

    def __call__(self, *args, **kwargs):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args, **kwargs)
            self.__cache[args] = obj
            return obj


# Example
class Spam(metaclass=Cashed):
    def __init__(self, name):
        print('Creating Spam({!r})'.format(name))
        self.name = name


