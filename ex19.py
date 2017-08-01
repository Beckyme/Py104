# -*- coding:utf-8 -*-
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# 定义函数cheese_and_crackers并赋予其参数cheese_count, boxes_of_crackers
	print "You have %d cheeses!" % cheese_count
	# 输出“You have 整数型格式化字符 cheeses！” 该字符引用 cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	# 输出“You have 整数型格式化字符 boxes of crackers!" 该字符引用 boxes_of_crackers
	print "Man that's enough for a party!"
	# 输出“Man that's enough for a party!"
	print "Get a blanket.\n"
	#输出“Get a blanket.换行


print "We can just give the function numbers directly:"
# 输出"We can just give the fuction numbers directly:"
cheese_and_crackers(20, 30)
# 给cheese_and_crackers赋值20，30；输出时会输出之前定义的函数内容，其中的整数型格式化字符会被打印成20,30


print "OR, we can use variables from our script:"
# 输出"OR, we can use variables from our script:"
amount_of_cheese = 10
# 给变量amount_of_cheese赋值10
amount_of_crackers = 50
# 给变量amount_of_crackers赋值50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# 输出cheese_and_crackers并赋予其参数amount_of_cheese和amount_of_crackers
# 输出时会输出之前定义的函数内容，其中的整数型格式化字符会被打印成10,50


print "We can even do math inside too:"
# 输出"We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
# 给变量amount_of_cheese赋值表达式；输出时会输出之前定义的函数内容，其中的整数型格式化字符会被打印成30，11


print "And we can combine the two, variables and math:"
# 输出"And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
# 给变量amount_of_cheese赋值变量+表达式，输出时会输出之前定义的函数内容，其中的整数型格式化字符会被打印成110,1050