# -*- coding:utf-8 -*-
#1.已经在ex3.py完成。
#2.在powershell中运行过了。
#3.
from __future__ import division
a = 244158112/1024
print a

'''
4.浮点数是属于有理数中某特定子集的数的数字表示，在计算机中用以近似表示任意某个实数。
浮点数在表示数字的时候直接阶段，而不是四舍五入得到的整数，如8/3得整数2。
python能很好地支持浮点数运算，但是python中浮点数是用二进制分数进行表示的。
通常代码中的浮点数是由十进制分数表示，因此在其转换为二进制分数时面临着尾数上的截断误差。
网上有很多浮点数精度的文章可供参考。
'''
# 5
print "I will now count my chickens:"

# 输出母鸡的数量，先乘除后加减。
print "Hens", 25.0 + 30 / 6
# 输出公鸡的数量，%是取余数，和乘除的优先级一样。
print "Roosters", 100.0 - 25 * 3 % 4
# 输出"Now I will count the eggs:"
print "Now I will count the eggs:"

# 3+2+1-5+0-0+6
print 3.0 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

# 输出"Is it true that 3 + 2 < 5 - 7?"
print "Is it true that 3 + 2 < 5 - 7?"

# If print <, >, <=, >=, print out TRUE or FALSE.
print 3 + 2 < 5 - 7

# If the calculate in a print "", just print the formula.
print "What is 3.0 + 2?", 3 + 2
print "What is 5.0 - 7?", 5 - 7

# print string
print "Oh, that's why it's False."
# print string
print "How about some more."
# 输出布尔值。
print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5<= -2