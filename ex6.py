# -*- coding:utf-8 -*-

# 给x赋值str，%d是将10转换为有符号整数的格式化字符，如果添加的是10.0（浮点数），输出时也会输出10（整数）。
x = "There are %d types of people." % 10
# 给binary赋值str。
binary = "binary"
# 给do_not赋值str。
do_not = "don't"
# 给y赋值str， %s是输出字符串的格式化字符，输出binary和do_not变量。
y = "These who know %s and those who %s." % (binary, do_not)

# 输出x和y
print x
print y

# 输出str，%r用rper()方法处理对象，打印时能够重现它所代表的对象。
print "I said: %r." % x
# 输出str，%s用str()方法处理对象，输出str，更适合面向用户。
print "I also said: %s'." % y

# 给hilarious赋予布尔值False。
hilarious = False
# 给joke_evaluation赋值str。
joke_evaluation = "Isn't that joke so funny?! %r"

# 输出str。
print joke_evaluation % hilarious

# 给w赋值str。
w = "This is the left side of..."
# 给e赋值str。
e = "a string with a right side."

# 输出w + e，+ 可以连接字符串。
print w + e