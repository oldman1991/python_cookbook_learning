# coding=utf-8
"""
筛选列表中的元素
"""
mylist = [1, 2, 3, -1, 5, -7]
pos = (n for n in mylist if n > 0)  # generator object 返回的是一个生成器


# print (pos)


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

values = ['1','2','4','-1','w','-o']
ivals = list(filter(is_int,values))
print (ivals)



