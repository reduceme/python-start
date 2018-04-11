#!/usr/bin/python
# -*- coding: UTF-8 -*-

for letter in 'Python':
    print '当前字母：', letter

fruits = ['apple', 'mango', 'banana']
for fruit in fruits:
    print '当前水果：', fruit

# 通过序列索引迭代
for index in range(len(fruits)):
    print '当前水果：', fruits[index]

# for else
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print '%d 等于 %d * %d' % (num, i, j)
            break  # 跳出当前循环
    else:
        print num, '是一个质数'
