# coding=utf-8

"""
从字典中提取一个子集
"""
price = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# Make a dictionary of all price over 200
p1 = {key: value for key, value in price.items() if value > 200}

# Make a dictionary of tech stocks
tech_names = {'APPLE', 'IBM', 'HPQ', 'MSFT'}
P2 = {key: value for key, value in price.items() if key in tech_names}

p1 = dict((key, value) for key, value in price.items() if value > 200)  # 但是这种解决方案要比上一种慢1.6倍

# eg:Make a dictionary of tech stocks
p2 = {key: price[key] for key in price.keys() & tech_names}  # 但是这种解决方案要比上一种慢1.6倍
