#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 必选参数、默认参数、可变参数、关键字参数和命名关键字参数

def hello(greeting, *args):
    if (len(args) == 0):
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ','.join(args)))


hello('Hi')
hello('Hi', 'Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam')

name = ('Bart', 'Lisa')
# hello('hello', *name)
hello('hello', *name)
