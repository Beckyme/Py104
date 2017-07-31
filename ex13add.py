# -*- coding:utf-8 -*-
from sys import argv

name, age, hobby = argv

print "The file name is:", name
print "Your age is:", age
print "Your hobby is:", hobby

'''
ValueError: not enough values to unpack (expected 3, got 1)
当给出的参数不足时，错误提示就会提示参数不足。
并在括号内提示需要几个参数，输入了几个参数。
'''



