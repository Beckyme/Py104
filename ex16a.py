# -*- coding:utf-8 -*-

from sys import argv

script, filename = argv

txt = open(filename,"w")

print "Truncating the file. Goodbye!"
txt.truncate()

print "Please write something to celebrate the New Year."

wish1 = raw_input("Wish1: ")
wish2 = raw_input("Wish2: ")
wish3 = raw_input("Wish3: ")

print "I'm going to write these to the file."

txt.write("%r\n%r\n%r" % (wish1, wish2, wish3))

print "Then I'll closed this file."
print txt.close()


# 可以运行但输出结果每行都会被加单引号，无论我是使用单引号还是使用双引号将字符串扩起。