#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        print(product)
        return product
    return fact_iter(num - 1, num * product)


fact(5)

list = [x * x for x in range(1, 11)]
print(list)

list_two = [m + n for m in 'ABC' for n in 'DEF']
print(list_two)
