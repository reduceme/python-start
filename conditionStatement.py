#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 例1：if 基本用法

flag = False
name = 'alen'
if name == 'python':
    flag = True
    print 'welcome boss'
else:
    print name

num = 5
if num == 3:
    print 'num = 3'
elif num == 4:
    print 'num = 4'
elif num == 5:
    print '5'
else:
    print num

num = 9
if num > 0 and num < 10:
    print 'hello'

num = 8
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print 'hello'
else:
    print 'undefine'