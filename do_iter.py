#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable, Iterator


def g():
    yield 1
    yield 2
    yield 3


print(isinstance([1, 2, 3], Iterable))
print(isinstance('abc', Iterable))
print(isinstance(123, Iterable))
print(isinstance(g(), Iterable))

print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))
print('Iterator? \'abc\':', isinstance('abc', Iterator))
print('Iterator? 123:', isinstance(123, Iterator))
print('Iterator? g():', isinstance(g(), Iterator))

# iter list
for x in [1, 2, 3, 4, 5, 6]:
    print(x)

for x in iter([1, 2, 3, 4, 5]):
    print(x)
