# -*- coding:utf-8 -*-
from sys import argv
# 将sys模组import进argv

script, input_file = argv
# 将script和input_file赋值给argv

def print_all(f):
	print f.read()
	# 定义函数print_all并给其赋值f，f代表了一个文件
	# 输出f文件中的内容
	
def rewind(f):
	f.seek(0)
	# 定义函数rewind并给其赋值f，f代表了一个文件
	# seek(0)代表回到文件开头
	
def print_a_line(line_count, f):
	print line_count, f.readline()
	# 定义函数print_a_line并给其赋值line_count和f，f代表了一个文件
	# 输出line_count, f文件中所读取的那行
	
current_file = open(input_file)
# current_line赋值为打开input_file(输入的文件)

print "First let's print the whole file:\n"
# 输入"First let's print the whole file:换行"

print_all(current_file)
# print_all赋值为current_file(即打开所输入文件)

print "Now let's rewind, kind of like a tape."
# 输入"Now let's rewind, kind of like a tape."

rewind(current_file)
# rewind赋值为current_file(即打开所输入文件，并回到开头位置)

print "Let's print three lines:"
# 输入"Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)
# current_line赋值为1
# print_a_line赋值为current_line和current_file（即先输出1，再输出1行所在内容）

current_line = current_line + 1
print_a_line(current_line, current_file)
# current_line赋值为自+1
# print_a_line赋值为current_line和current_file（即先输出2，再输出2行所在内容）

current_line = current_line + 1
print_a_line(current_line, current_file)
# current_line赋值为自+1
# print_a_line赋值为current_line和current_file（即先输出3，再输出3行所在内容）