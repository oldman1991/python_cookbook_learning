# coding=utf-8
import pkgutil

for item in pkgutil.iter_modules(['.']):
    print(item)