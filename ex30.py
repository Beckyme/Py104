# -*- coding:utf-8 -*-
people = 30
# 定义people变量赋值30
cars = 40
# 定义cars变量赋值40
buses = 15
# 定义buses变量赋值15


if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."
"""
	如果 cars > people，则输出We should take the cars.
	如果 cars < people，则输出We should not take the cars.
	其他则输出We can't decide.
"""
	
if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."
"""
	如果 buses > cars，则输出That's too many buses.
	如果 buses < cars，则输出Maybe we could take the buses.
	其他则输出We still can't decide.
"""
	
if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."
"""
	如果people > buses，则输出Alright, let's just take the buses.
	其他则输出Fine, let's stay home then.
"""