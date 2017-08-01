# -*- coding:utf-8 -*-
i = 1
numbers = []

while i < 100:
	print "At the top i is %d" % i
	numbers.append(i)
	
	n = int(raw_input("Give me a number"))
	
	i = i + n
	
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	
print "The numbers: "

for num in numbers:
	print num