# coding:utf-8
from sys import argv
# 将sys模组import进argv

script, filename = argv
# 将script和filename赋值给grav

txt = open(filename)
# 变量txt等于打开（文件名）的文件

print "Here's your file %r:" % filename
# 输出Here's your file 文件名
print txt.read()
# 输出txt变量内文件所被读取的内容

print "I'll also ask you to type it again:"
file_again = raw_input("> ")
# 输出I'll also ask you to type it again:
# file_again变量等于>用户输入的文件名

txt_again = open(file_again)
# txt_again变量等于打开file_again中用户输入的文件名所代表的文件

print txt_again.read()
# 输出txt_again变量内文件所被读取的内容

txt_again.close()
txt.close()

