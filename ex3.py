# -*- coding:utf-8 -*-

# 输出"I will now count my chickens:"
print "I will now count my chickens:"

# 输出母鸡的数量，先乘除后加减。
print "Hens", 25 + 30 / 6
# 输出公鸡的数量，%是取余数，和乘除的优先级一样。
print "Roosters", 100 - 25 * 3 % 4
# 输出"Now I will count the eggs:"
print "Now I will count the eggs:"

# 3+2+1-5+0-0+6
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

# 输出"Is it true that 3 + 2 < 5 - 7?"
print "Is it true that 3 + 2 < 5 - 7?"

# If print <, >, <=, >=, print out TRUE or FALSE.
print 3 + 2 < 5 - 7

# If the calculate in a print "", just print the formula.
print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

# print string
print "Oh, that's why it's False."
# print string
print "How about some more."
# 输出布尔值。
print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5<= -2

# 整数运算结果为整数，浮点数运算结果为浮点数，整数浮点数混合运算结果为浮点数
# 不会 from __future__ import division 实除法模块，下行再输入整数运算，可得到浮点值
#int("4.56")==4  浮点数转换为整数，简单取整，不涉及四舍五入。
#float(5)==5.0 整数转换为浮点数
#str(0xcc)==‘204’ 整数和浮点数转换为字符串。
