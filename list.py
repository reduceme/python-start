#!/usr/bin/python

list1 = ['physics', 'computer', 1211, 208]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print 'list1[0]:', list1[0]
print list2[1:5]

list1.append('google')
print list1

# del list1[0]
list1.remove(list1[0])
print list1

