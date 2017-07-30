# -*- coding:utf-8 -*-
"I am 6'2\" tall." # 将字符串中的双引号转义
'I am 6\'2" tall.' # 将字符串中的单引号转义
"转义序列\"escape sequences\"" # 将字符串中的双引号转义

tabby_cat = "\tI'm tabbed in." # \t横向制表符  \v纵向制表符
persian_cat = "I'm split\non a line." # \n换行   \r回车
backslash_cat = "I'm \\ a \\ cat."

# 给变量赋值时也可用'''赋值多行str，内含\t\n转义字符。
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# 输出变量。
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
