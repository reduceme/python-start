#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import math


def getTime():
    year = time.localtime(time.time()).tm_year
    print(year)


getTime()

print(abs(-2))
print(int('123'))

x = abs(100)
y = abs(-20)
print(x, y)
print('max(1,2,3) = ', max(1, 2, 3))
print('min(1,2,3) = ', min(1, 2, 3))
print('sum([1,2,3]) = ', sum([1, 2, 3]))