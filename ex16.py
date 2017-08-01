# -*- coding:utf-8 -*-
from sys import argv
# 将sys模组import进argv

script, filename = argv
# 将script和filename赋值给grav

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# 输出We're going to erase文件名
# 输出If you don't want that, hit CTRL-C (^C)
# 输出If you do want that, hit RETURN.

raw_input("?")
# 输入提示符？输出

print "Opening the file..."
target = open(filename, 'w')
# 输出Opening the file...
# 变量target被赋予打开文件名的文件使其处于可编辑模式

print "Truncating the file.  Goodbye!"
target.truncate()
# 输出Truncating the file. Goodbye!
# 将target变量所被赋予的文件内容清空

print "Now I'm going to ask you for three lines."
# 输出Now I'm going to ask you for three lines.

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
# line1被赋值为所输入的内容，提示内容为line1：
# line2被赋值为所输入的内容，提示内容为line2：
# line3被赋值为所输入的内容，提示内容为line3：

print "I'm going to write these to the file."
# 输出I'm going to write these to the file.

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# 在target变量所被赋予的文件内写入line1变量所被输入的内容
# 在target变量所被赋予的文件内换行
# 在target变量所被赋予的文件内写入line2变量所被输入的内容
# 在target变量所被赋予的文件内换行
# 在target变量所被赋予的文件内写入line3变量所被输入的内容
# 在target变量所被赋予的文件内换行

print "And finally, we close it."
target.close()
# 输出And finally, we close it.
# 将target变量所被赋予的文件关闭