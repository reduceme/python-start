#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def f(x):
    return x * x


def fn(x, y):
    return x * 10 + y


print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
