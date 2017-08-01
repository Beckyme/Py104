# -*- coding:utf-8 -*-

i = 0
numbers = []
n = 23
for i in range(0, 101, n):
	print "At the top i is %d" % i
	numbers.append(i)
	
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	
print "The numbers: "

for num in numbers:
	print num
