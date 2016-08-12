# coding=utf-8

"""
从序列中移除重复且保持元素箭顺序不变
"""


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe2(items, key=None):
    """
    复杂对象的去重
    """
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
            print(seen)


# a=dedupe([1,2,2,2,3,2,4,5])
# for item in a:
#     print(item)
# b = dedupe2(items=[{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}],
#             key=lambda d: (d['x'], d['y']))
# for item in b:
#     print(item)
# a=slice(5,10,2)
# s = 'HelloWorldnihao'
# print(a.indices(len(s)))
# for item in range(*a.indices(len(s))):
#     print (item)